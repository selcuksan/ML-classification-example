from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.ml.feature import StringIndexer, VectorAssembler, OneHotEncoder
from pyspark.ml import Pipeline
from pyspark.ml.classification import GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

spark = SparkSession \
    .builder \
    .appName("classification-example") \
    .getOrCreate()

df = spark.read.csv(r"bank.csv", inferSchema=True, header=True)

numeric_features = [feature for feature, dtype in df.dtypes if dtype == 'int']
numeric_data = df.select(*numeric_features).toPandas()
print(abs(numeric_data.corr()))

sns.pairplot(numeric_data)

sns.heatmap(abs(numeric_data.corr()))

plt.show()

df = df.select('age', 'job', 'marital', 'education',
               'default', 'balance', 'housing', 'loan',
               'contact', 'duration', 'campaign', 'pdays',
               'previous', 'poutcome', 'deposit')
cols = df.columns

categoricalColumns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome']
stages = []
for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + 'Index')
    encoder = OneHotEncoder(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    stages += [stringIndexer, encoder]
label_stringIdx = StringIndexer(inputCol='deposit', outputCol='label')
stages += [label_stringIdx]
numericCols = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous']
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler]

pipeline = Pipeline(stages=stages)
pipelineModel = pipeline.fit(df)
df = pipelineModel.transform(df)
selectedCols = ['label', 'features'] + cols
df = df.select(selectedCols)

train, test = df.randomSplit([0.7, 0.3], seed=2018)
print(train.count())
print(test.count())



gbt = GBTClassifier(maxIter=10)
gbt_model = gbt.fit(train)
predictions = gbt_model.transform(test)


evaluator = BinaryClassificationEvaluator()
score = evaluator.evaluate(predictions,{
    evaluator.metricName: "areaUnderROC"
})
print("model başarısı: ", score)


paramGrid = (ParamGridBuilder()
    .addGrid(gbt.maxDepth, [2, 4, 6])
    .addGrid(gbt.maxBins, [20, 60])
    .addGrid(gbt.maxIter, [10, 20])
    .build()
)
cv = CrossValidator(estimator=gbt,estimatorParamMaps=paramGrid, evaluator=evaluator, numFolds=5)


cv_model = cv.fit(train)
final_predictions = cv_model.transform(test)
final_score = evaluator.evaluate(
    final_predictions, params={
        evaluator.metricName:"areaUnderROC"
    }
)
print('Model Tuning sonrası final modeli başarısı: ', final_score)