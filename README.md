# Apache Spark Nedir

* Apache Spark, veri çalışanlarının veri kümelerine hızlı yinelemeli erişim gerektiren akış, makine öğrenmesi veya SQL iş yüklerini verimli bir şekilde yürütmelerini sağlayan zarif ve etkileyici geliştirme API’lerine sahip hızlı, bellek içi bir veri işleme motorudur.

* Apache Spark'ın ana özelliği, bir uygulamanın işlem hızını artıran bellek içi küme hesaplamadır. Spark tüm kümeleri programlamak için örtük veri paralelliği ve hata toleransı ile bir arayüz sağlar. 
Toplu iş uygulamaları, yinelemeli algoritmalar, etkileşimli sorgular ve akış gibi çok çeşitli iş yüklerini kapsayacak şekilde tasarlanmıştır.

    - Hızlıdır
    Spark, büyük ölçekli veri işleme için kullanılan Hadoop MapReduce'dan 100 kat daha hızlı çalışır. Bu hıza kontrollü bölümleme yoluyla da ulaşabilir.

    - Güçlü Önbellekleme
    Basit programlama katmanı, güçlü önbellekleme ve disk kalıcılığı yetenekleri sağlar.

    - Gerçek zamanlılık
    Bellek içi hesaplama nedeniyle Gerçek Zamanlı hesaplama ve düşük gecikme süresi sunar.

    - Dil Desteği
    Spark, Java, Scala, Python ve R için üst düzey API'ler sunar.
    
  
## Spark Ekosistemi

* Spark Core
  Spark Core, büyük ölçekli paralel ve dağıtılmış veri işleme için temel motordur. Sahip olduğu kütüphaneler ile, akış , SQL ve makine öğrenmesi gibi çeşitli iş yüklerine izin verir. 
  Bellek yönetimi ve hata kurtarma, bir kümedeki işleri planlamak, dağıtmak ve izlemek ve depolama sistemleriyle etkileşimden sorumludur.
  
- Spark Streaming
  Spark Streaming, gerçek zamanlı akış verilerini işlemek için kullanılan Spark bileşenidir. Gerçek zamanlı veri akışlarının yüksek verimli işlenmesini sağlar.
  
* Spark SQL
  Spark'ın işlevsel programlama API'si ile ilişkisel işlemeyi birleştiren yeni bir modül. SQL veya Hive Query Language aracılığıyla veri sorgulamayı destekler. RDBMS veritabanları için Spark SQL performans arttırıcı bir çözüm sunar.
  
* GraphX
GraphX, grafikler ve grafik paralel hesaplamalar için Spark API'dir.

* MLlib (Machine Learning)
MLlib, Makine Öğrenimi Kütüphanesi'nin kısaltmasıdır. Spark MLlib, Apache Spark'da makine öğrenmesi için kullanılır.



# Classification (Sınıflandırma) problemi nedir

* Makine öğreniminde sınıflandırma, öğeleri önceden kategorize edilmiş bir eğitim veri kümesine göre kategorilere ayırma sürecidir. Sınıflandırma, denetimli bir öğrenme algoritması olarak kabul edilir.

* Sınıflandırma algoritmaları, yeni bir öğenin tanımlanan kategorilerden birine girme olasılığını hesaplamak için eğitim verilerinin kategorizasyonunu kullanır.

        -   Sınıflandırma algoritmalarının bilinen bir örneği, gelen e-postaların “spam” veya “spam değil” şeklinde filtrelenmesidir.

## Farklı sınıflandırma algoritmalarından bazıları şunlardır;
    -   KNN ((K-Nearest Neighbors)
    -   Karar Ağaçları (Decision Trees)
    -   SVM (Support Vector Machine)
    -   Naive Bayes
