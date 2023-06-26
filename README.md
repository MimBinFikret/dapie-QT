```markdown
# Dapie

Dapie, PyQt5 ve Docker kütüphanelerini kullanarak oluşturulmuş bir Docker konteynır listeleme uygulamasıdır. Bu uygulama, bilgisayarınızdaki Docker konteynırlarını listeleyerek kullanıcıya görüntüler.

## Gereksinimler

- Python 3.x
- PyQt5
- Docker Python modülü

## Kurulum

1. Projeyi klonlayın veya ZIP olarak indirin.

2. Terminali açın ve projenin kök dizinine gidin.

3. Gerekli Python paketlerini yüklemek için aşağıdaki komutu çalıştırın:

   ```bash
   make
   ```

   Bu komut, Makefile'ı çalıştırarak gereklilikleri yükler ve Python betiğinizi derler.

## Kullanım

1. Terminali açın ve projenin kök dizinine gidin.

2. Aşağıdaki komutu çalıştırarak uygulamayı başlatın:

   ```bash
   ./dapie
   ```

3. Uygulama başlatıldığında, Docker konteynırlarınızı gösteren bir pencere görüntülenecektir.

4. Çıkış yapmak için "Çıkış" butonuna tıklayın veya pencereyi kapatın.

## Makefile Kullanımı

Proje, bir Makefile içerir. Makefile, gereklilikleri yüklemeyi ve Python betiğinizi derlemeyi otomatikleştirir.

- Gereklilikleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

  ```bash
  make
  ```

- Derlenmiş bir sürüm oluşturmak için aşağıdaki komutu kullanabilirsiniz:

  ```bash
  make dapie
  ```

- Oluşturulan dosyaları temizlemek için aşağıdaki komutu kullanabilirsiniz:

  ```bash
  make clean
  ```

## Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına bakın.

## Katkı

Eğer bu projeye katkıda bulunmak isterseniz, lütfen CONTRIBUTING dosyasına bakın.

## Sorun Bildirme

Herhangi bir sorunla karşılaşırsanız, lütfen bir GitHub sorunu açın veya bana e-posta gönderin.
