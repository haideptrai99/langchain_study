# Làm quen với Python - Part 2 - Python package & module


Trong phần 2 này, chúng ta sẽ cùng nhau tìm hiểu thêm về python package và module.

# 1\. Python packages

Một cách đơn giản nhất, nếu **module** chỉ đơn thuần là **file** có đuôi là `.py`, thì **package** có thể xem là **directory** chứa các modules.

[Packages](https://docs.python.org/3/tutorial/modules.html#tut-packages) là phương pháp để quản lý python's module namspace bằng cách sử dụng "**dotted module names**". Ví dụ, khi gõ module name `A.B`, điều này có nghĩa là ta đang chỉ định tới **module B** ở bên trong **package A**.

Tương tự như việc sử dụng module để giúp người viết module không phải lo lắng là bị **trùng tên biến/hàm** ở các module của người khác viết, việc sử dụng **dotted module names** sẽ giúp người viết _multi-module packages_ như là NumPy hay Pillow không phải lo lắng về việc bị **trùng tên module** với người khác.

# 2\. `Import` statement

Giả sử như bạn muốn design một collection of modules ( a "package") để xử lý các sound files và sound data. Các sound file này sẽ có rất nhiều format khác nhau (thông thường được nhận biết thông qua extension của chúng, ví dụ: `.wav`, `.aiff`, `.au`), vì vậy bạn cần phải create và maintain a **growing** collection of modules để chuyển đổi giữa các formats khác nhau.

Tiếp theo, sẽ có rất nhiều tác vụ mà bạn muốn thực hiện trên sound data (ví dụ như mixing, thêm echo, áp dụng equalizer function, tạo ra các hiệu ứng âm thanh,..), như vậy, khả năng là chúng ta sẽ phải viết một loạt các module kéo dài vô tận để thực hiện các tác vụ này. Dưới đây là một cấu trúc của package mà chúng ta có thể sử dụng:

```none
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```

Đã sao chép ✔️

File `__init__.py` bắt buộc phải có để Python xem một directory là một package.

Trong trường hợp đơn giản nhất, thì `__init.py__` có thể chỉ là một file rỗng, nhưng nó có thể được sử dụng để chạy các code khởi tạo, hoặc là để set giá trị cho biến `__all__` , sẽ được mô tả sau.

Người dùng của package có thể import riêng rẽ từng module, ví dụ:

```py
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
```

Đã sao chép ✔️

Một cách khác để import cái submodule:

```py
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)
```

Đã sao chép ✔️

Hoặc ta có thể tiến xa hơn nữa, import thẳng cái function vào symbol table luôn:

```py
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
```

Đã sao chép ✔️

**So sánh `from package import item` và `import item.subitem.subsubitem`**

Với `from package import item`, cái **item** sẽ có thể hoặc là ✔ submodule, hoặc là ✔ subpackage, hoặc có thể là ✔ function, ✔ class hoặc ✔ variable.

Về thứ tự, thì import statement sẽ kiểm tra xem cái tên đó có phải là một định nghĩa trong cái package đó hay không (function, class, variable), nếu không có, thì nó sẽ ngầm hiểu đây là module và thử load module.

Với `import item.subitem.subsubitem`, mỗi item trừ cái cuối cùng, bắt buộc phải là một package, cái cuối cùng sẽ có thể hoặc là một ✔ module hoặc là một ✔ package, nhưng nó không thể là ❌ function, ❌ class, ❌ variable.

# 3\. Package Relative Imports

Khi mà package được cấu trúc thành các subpackages (như ví dụ cái `sound` package), thì bạn sẽ có thể sử dụng **absolute import** để refer tới các **submodules** bên trong **siblings packages**.

Ví dụ, nếu module `sound.filters.vocoder` cần sử dụng `echo` module ở trong `sound.effects` package, ta có thể viết `from sound.effects import echo`.

Hoặc, ta có thể viết **releative import**, vẫn sử dụng dạng `from module import name` . Nhưng chúng ta sẽ sử dụng **leading dots** để chỉ ra **current** và **parent package** có tham gia vào quá trình import. Ví dụ, như ta đang đứng bên trong `surround` module, ta có thể import như sau:

```py
from . import echo
from .. import formats
from ..filters import equalizer
from .echo import echofilter
```

Đã sao chép ✔️

Note: với **absolute import** thì ta có thể sử dụng hoặc là `import <>` hoặc là `from <> import <>`. Nhưng `relative import` sẽ chỉ dùng dạng `from <> import <>`. Lý do là bởi vì, với:

```none
import XXX.YYY.ZZZ
```

Đã sao chép ✔️

thì `XXX.YYY.ZZZ` là một usable expression, nhưng `.XXX` thì _không_ phải là một _valid_ expression.

# 4\. `__all__` variable

Có một câu hỏi, là chuyện gì xảy ra khi người dùng viết `from sound.effects import *`?

Trường hợp lý tưởng nhất, là bên trong file `__init__.py` của package, có cung cấp danh sách tên các modules sẽ được import, sử dụng `__all__` variable. Ví dụ

```py
__all__ = ["echo", "surround", "reverse"]
```

Đã sao chép ✔️

Khi đó, interpreter sẽ chỉ import các module có name được cung cấp trong danh sách này.

Trường hợp biến `__all__` không được định nghĩa, câu lệnh `from sound.effects import *` sẽ KHÔNG import tất cả submodules của package sound.effects vào. Nó chỉ đảm bảo là package `sound.effects` được import, chạy tất cả code bên trong file `__init__.py`, và import tất cả các names được định nghĩa trong package. Những names này bao gồm tất cả function, class, variable được định nghĩa bên trong file `__init__.py` và các submodules được explicitly loaded.

Tới đây, thì ta sẽ thấy hai cách dưới đây là tương đương nhau:

```py
import sound.effects.echo
import sound.effects.surround
import sound.effects.reverse

Hoặc

from sound.effects import *
```

Đã sao chép ✔️

Tuy cả 2 cách đều cho ra kết quả như nhau, `import *` vẫn được xem là **bad practice**. Và `from package import specific_submodule` là cách được recommended.

[Django](/tags/django) [Python](/tags/python)

  

All rights reserved

*   Báo cáo
*   Thêm vào series của tôi

#### Mục lục

* * *

*   [1\. Python packages](#_1-python-packages-0)
*   [2\. `Import` statement](#_2-import-statement-1)
*   [3\. Package Relative Imports](#_3-package-relative-imports-2)
*   [4\. `__all__` variable](#_4-__all__-variable-3)

  

### **Bài viết liên quan**

[Python và xu hướng trong tương lai](/p/python-va-xu-huong-trong-tuong-lai-GrLZDeMnlk0 "Python và xu hướng trong tương lai")

[Thu Hoài](/u/hoaittt)

5 phút đọc

1.6K 1 0

0

[Tìm hiểu Django framwork (Python)](/p/tim-hieu-django-framwork-python-RQqKLw6r57z "Tìm hiểu Django framwork (Python)")

[Viet Anh](/u/Nguyen.Viet.AnhB)

8 phút đọc

1.1K 1 1

3

[Python: Quản lý package (Dependency Management) - Đơn giản!](/p/python-quan-ly-package-dependency-management-don-gian-r1QLx9zgVAw "Python: Quản lý package (Dependency Management) - Đơn giản!")

[PTITQuyNA](/u/anhquyqt03)

13 phút đọc

1.5K 1 1

1

[9 thủ thuật nhanh cho người bắt đầu học Python](/p/9-thu-thuat-nhanh-cho-nguoi-bat-dau-hoc-python-l0rvmxakGyqA "9 thủ thuật nhanh cho người bắt đầu học Python ")

[nguyễn khắc hải](/u/nguyenhai)

0 phút đọc

2.5K 1 0

4

[Kiểu dữ liệu và các kiểu dữ liệu trong Python](/p/kieu-du-lieu-va-cac-kieu-du-lieu-trong-python-4dbZNgGvlYM "Kiểu dữ liệu và các kiểu dữ liệu trong Python")

[Nguyễn Hữu Kim](/u/huukimit)

6 phút đọc

34.8K 6 0

2

[Python #1: Comprehension](/p/python-1-comprehension-LzD5dbgoZjY "Python #1: Comprehension")

[Pham Quang Hung](/u/hwng)

3 phút đọc

336 5 1

3

[Giới thiệu sqlalchemy trong python(part 1)](/p/gioi-thieu-sqlalchemy-trong-pythonpart-1-Q7eERE9rRgNj "Giới thiệu sqlalchemy trong python(part 1)")

[Tran Van Nhat](/u/tran.van.nhat)

6 phút đọc

15.7K 4 2

5

[Thực hiện cuộc gọi điện thoại bằng Python](/p/thuc-hien-cuoc-goi-dien-thoai-bang-python-AoDGYNpBRvg "Thực hiện cuộc gọi điện thoại bằng Python")

[Phuc Le Cong](/u/le.cong.phuc)

2 phút đọc

2.8K 4 0

2

[Signal trong Python](/p/signal-trong-python-Qbq5QNpmKD8 "Signal trong Python")

[Ha Hao Minh](/u/minhhahao)

4 phút đọc

3.2K 4 2

4

[Python Social Auth with Facebook, Google](/p/python-social-auth-with-facebook-google-924lJLVNKPM "Python Social Auth with Facebook, Google")

[Pham Van Duc B](/u/Phamduc97)

3 phút đọc

2.0K 3 0

9

[Phân biệt chính giữa Python 2.7.x và Python 3.x](/p/phan-biet-chinh-giua-python-27x-va-python-3x-OeVKBygM5kW "Phân biệt chính giữa Python 2.7.x và Python 3.x")

[nguyen chi thanh](/u/nguyen.chi.thanh)

4 phút đọc

4.5K 3 0

0

[Sử dụng List Comprehensions trong python](/p/su-dung-listcomprehensions-trong-python-OeVKBDdylkW "Sử dụng List	Comprehensions trong python")

[SonNT](/u/NguyenThaiSon)

2 phút đọc

1.7K 2 0

0

[Python và xu hướng trong tương lai](/p/python-va-xu-huong-trong-tuong-lai-GrLZDeMnlk0 "Python và xu hướng trong tương lai")

[Thu Hoài](/u/hoaittt)

5 phút đọc

1.6K 1 0

0

[Tìm hiểu Django framwork (Python)](/p/tim-hieu-django-framwork-python-RQqKLw6r57z "Tìm hiểu Django framwork (Python)")

[Viet Anh](/u/Nguyen.Viet.AnhB)

8 phút đọc

1.1K 1 1

3

[Python: Quản lý package (Dependency Management) - Đơn giản!](/p/python-quan-ly-package-dependency-management-don-gian-r1QLx9zgVAw "Python: Quản lý package (Dependency Management) - Đơn giản!")

[PTITQuyNA](/u/anhquyqt03)

13 phút đọc

1.5K 1 1

1

[9 thủ thuật nhanh cho người bắt đầu học Python](/p/9-thu-thuat-nhanh-cho-nguoi-bat-dau-hoc-python-l0rvmxakGyqA "9 thủ thuật nhanh cho người bắt đầu học Python ")

[nguyễn khắc hải](/u/nguyenhai)

0 phút đọc

2.5K 1 0

4

[Kiểu dữ liệu và các kiểu dữ liệu trong Python](/p/kieu-du-lieu-va-cac-kieu-du-lieu-trong-python-4dbZNgGvlYM "Kiểu dữ liệu và các kiểu dữ liệu trong Python")

[Nguyễn Hữu Kim](/u/huukimit)

6 phút đọc

34.8K 6 0

2

[Python #1: Comprehension](/p/python-1-comprehension-LzD5dbgoZjY "Python #1: Comprehension")

[Pham Quang Hung](/u/hwng)

3 phút đọc

336 5 1

3

[Giới thiệu sqlalchemy trong python(part 1)](/p/gioi-thieu-sqlalchemy-trong-pythonpart-1-Q7eERE9rRgNj "Giới thiệu sqlalchemy trong python(part 1)")

[Tran Van Nhat](/u/tran.van.nhat)

6 phút đọc

15.7K 4 2

5

[Thực hiện cuộc gọi điện thoại bằng Python](/p/thuc-hien-cuoc-goi-dien-thoai-bang-python-AoDGYNpBRvg "Thực hiện cuộc gọi điện thoại bằng Python")

[Phuc Le Cong](/u/le.cong.phuc)

2 phút đọc

2.8K 4 0

2

[Kiểu dữ liệu và các kiểu dữ liệu trong Python](/p/kieu-du-lieu-va-cac-kieu-du-lieu-trong-python-4dbZNgGvlYM "Kiểu dữ liệu và các kiểu dữ liệu trong Python")

[Nguyễn Hữu Kim](/u/huukimit)

6 phút đọc

34.8K 6 0

2

[Python #1: Comprehension](/p/python-1-comprehension-LzD5dbgoZjY "Python #1: Comprehension")

[Pham Quang Hung](/u/hwng)

3 phút đọc

336 5 1

3

[Giới thiệu sqlalchemy trong python(part 1)](/p/gioi-thieu-sqlalchemy-trong-pythonpart-1-Q7eERE9rRgNj "Giới thiệu sqlalchemy trong python(part 1)")

[Tran Van Nhat](/u/tran.van.nhat)

6 phút đọc

15.7K 4 2

5

[Thực hiện cuộc gọi điện thoại bằng Python](/p/thuc-hien-cuoc-goi-dien-thoai-bang-python-AoDGYNpBRvg "Thực hiện cuộc gọi điện thoại bằng Python")

[Phuc Le Cong](/u/le.cong.phuc)

2 phút đọc

2.8K 4 0

2

### **Bài viết khác từ You Nguyen**

[Autoload in PHP](/p/autoload-in-php-XL6lAdgNZek "Autoload in PHP")

[You Nguyen](/u/NguyenYou)

8 phút đọc

5.1K 7 2

11

[Metaclass in Python](/p/metaclass-in-python-gDVK24JnlLj "Metaclass in Python")

[You Nguyen](/u/NguyenYou)

6 phút đọc

3.1K 1 0

5

[How to Optimize React Hooks Performance - Tối ưu hiệu năng khi sử dụng React Hooks](/p/how-to-optimize-react-hooks-performance-toi-uu-hieu-nang-khi-su-dung-react-hooks-aWj533qQ56m "How to Optimize React Hooks Performance - Tối ưu hiệu năng khi sử dụng React Hooks")

[You Nguyen](/u/NguyenYou)

5 phút đọc

2.5K 4 0

9

[Làm quen với Python (Part 1 - Thiết lập môi trường)](/p/lam-quen-voi-python-part-1-thiet-lap-moi-truong-ORNZq17LZ0n "Làm quen với Python (Part 1 - Thiết lập môi trường)")

[You Nguyen](/u/NguyenYou)

6 phút đọc

2.6K 1 0

3

[Publish a npm package](/p/publish-a-npm-package-L4x5xPXm5BM "Publish a npm package")

[You Nguyen](/u/NguyenYou)

2 phút đọc

643 3 0

4

[Server Rendering React.js + Material UI web application](/p/server-rendering-reactjs-material-ui-web-application-WAyK86LklxX "Server Rendering React.js + Material UI web application")

[You Nguyen](/u/NguyenYou)

3 phút đọc

1.0K 3 0

2

[Generic (not specific) in Typescript](/p/generic-not-specific-in-typescript-gGJ59GrPZX2 "Generic (not specific) in Typescript")

[You Nguyen](/u/NguyenYou)

4 phút đọc

153 1 0

6

[IoC Container in PHP (Part 4) - Abstract to Concrete Resolution & Dependency Resolution](/p/ioc-container-in-php-part-4-abstract-to-concrete-resolution-dependency-resolution-gDVK2BY2KLj "IoC Container in PHP (Part 4) - Abstract to Concrete Resolution &  Dependency Resolution")

[You Nguyen](/u/NguyenYou)

2 phút đọc

145 1 0

3

[IoC Container in PHP (Part 3)](/p/ioc-container-in-php-part-3-aWj53BoQl6m "IoC Container in PHP (Part 3)")

[You Nguyen](/u/NguyenYou)

4 phút đọc

186 0 1

5

[IoC Container in PHP (Part 2)](/p/ioc-container-in-php-part-2-GrLZDJz35k0 "IoC Container in PHP (Part 2)")

[You Nguyen](/u/NguyenYou)

1 phút đọc

209 0 0

3

[IoC Container in PHP (Part 1)](/p/ioc-container-in-php-part-1-3P0lP0Lplox "IoC Container in PHP (Part 1)")

[You Nguyen](/u/NguyenYou)

3 phút đọc

620 0 1

4

[Windowing in ReactJS (Part1)](/p/windowing-in-reactjs-part1-jvEla7y6Kkw "Windowing in ReactJS (Part1)")

[You Nguyen](/u/NguyenYou)

3 phút đọc

618 1 1

3

[Autoload in PHP](/p/autoload-in-php-XL6lAdgNZek "Autoload in PHP")

[You Nguyen](/u/NguyenYou)

8 phút đọc

5.1K 7 2

11

[Metaclass in Python](/p/metaclass-in-python-gDVK24JnlLj "Metaclass in Python")

[You Nguyen](/u/NguyenYou)

6 phút đọc

3.1K 1 0

5

[How to Optimize React Hooks Performance - Tối ưu hiệu năng khi sử dụng React Hooks](/p/how-to-optimize-react-hooks-performance-toi-uu-hieu-nang-khi-su-dung-react-hooks-aWj533qQ56m "How to Optimize React Hooks Performance - Tối ưu hiệu năng khi sử dụng React Hooks")

[You Nguyen](/u/NguyenYou)

5 phút đọc

2.5K 4 0

9

[Làm quen với Python (Part 1 - Thiết lập môi trường)](/p/lam-quen-voi-python-part-1-thiet-lap-moi-truong-ORNZq17LZ0n "Làm quen với Python (Part 1 - Thiết lập môi trường)")

[You Nguyen](/u/NguyenYou)

6 phút đọc

2.6K 1 0

3

[Publish a npm package](/p/publish-a-npm-package-L4x5xPXm5BM "Publish a npm package")

[You Nguyen](/u/NguyenYou)

2 phút đọc

643 3 0

4

[Server Rendering React.js + Material UI web application](/p/server-rendering-reactjs-material-ui-web-application-WAyK86LklxX "Server Rendering React.js + Material UI web application")

[You Nguyen](/u/NguyenYou)

3 phút đọc

1.0K 3 0

2

[Generic (not specific) in Typescript](/p/generic-not-specific-in-typescript-gGJ59GrPZX2 "Generic (not specific) in Typescript")

[You Nguyen](/u/NguyenYou)

4 phút đọc

153 1 0

6

[IoC Container in PHP (Part 4) - Abstract to Concrete Resolution & Dependency Resolution](/p/ioc-container-in-php-part-4-abstract-to-concrete-resolution-dependency-resolution-gDVK2BY2KLj "IoC Container in PHP (Part 4) - Abstract to Concrete Resolution &  Dependency Resolution")

[You Nguyen](/u/NguyenYou)

2 phút đọc

145 1 0

3

[Publish a npm package](/p/publish-a-npm-package-L4x5xPXm5BM "Publish a npm package")

[You Nguyen](/u/NguyenYou)

2 phút đọc

643 3 0

4

[Server Rendering React.js + Material UI web application](/p/server-rendering-reactjs-material-ui-web-application-WAyK86LklxX "Server Rendering React.js + Material UI web application")

[You Nguyen](/u/NguyenYou)

3 phút đọc

1.0K 3 0

2

[Generic (not specific) in Typescript](/p/generic-not-specific-in-typescript-gGJ59GrPZX2 "Generic (not specific) in Typescript")

[You Nguyen](/u/NguyenYou)

4 phút đọc

153 1 0

6

[IoC Container in PHP (Part 4) - Abstract to Concrete Resolution & Dependency Resolution](/p/ioc-container-in-php-part-4-abstract-to-concrete-resolution-dependency-resolution-gDVK2BY2KLj "IoC Container in PHP (Part 4) - Abstract to Concrete Resolution &  Dependency Resolution")

[You Nguyen](/u/NguyenYou)

2 phút đọc

145 1 0

3

### **Bình luận**

Đăng nhập để bình luận

[![Avatar](https://images.viblo.asia/avatar/981ca3a0-44c1-4097-a633-87997c1e53fc.png)](/u/NguyenYou)

+4

•

Cỡ chữ

18px

Độ cao hàng

1.75

 Mặc định Toàn màn hình

Màu nền

Đặt lại

• • •

#### Tài nguyên

*   [Bài viết](/)
*   [Tổ chức](/organizations)
*   [Câu hỏi](/questions)
*   [Tags](/tags)
*   [Videos](/videos)
*   [Tác giả](/authors)
*   [Thảo luận](/discussion)
*   [Đề xuất hệ thống](/explore)
*   [Công cụ](https://about.viblo.asia/tools/)
*   [Machine Learning](https://machine-learning.viblo.asia)
*   [Trạng thái hệ thống](https://status.viblo.asia)

#### Dịch vụ

*    [![Viblo](/favicon.ico) Viblo](https://viblo.asia)

*    [![Viblo Code](/images/viblo-code.png) Viblo Code](https://code.viblo.asia)

*    [![Viblo CTF](/images/viblo-ctf.png) Viblo CTF](https://ctf.viblo.asia)

*    [![Viblo CV](/images/viblo-cv.png) Viblo CV](https://cv.viblo.asia)

*    [![Viblo Learning](/images/viblo-learn.png) Viblo Learning](https://learn.viblo.asia)

*    [![Viblo Partner](/images/viblo-partner.png) Viblo Partner](https://partner.viblo.asia)

*    [![Viblo Battle](/images/viblo-battle.png) Viblo Battle](https://battle.viblo.asia)

*    [![Viblo Interview](/images/viblo-interview.ico) Viblo Interview](https://interview.viblo.asia)

#### Ứng dụng di động

[![Get it on Google Play](https://play.google.com/intl/en_us/badges/images/generic/en_badge_web_generic.png)](https://play.google.com/store/apps/details?id=com.sun.viblo.android) [![Download on the App Store](/_nuxt/img/app-store-badge.8c4986ee4828b47d16f5cd694ef065f2.svg)](https://itunes.apple.com/us/app/viblo/id1365286437)

![QR code](/_nuxt/img/app-qr.c5ca206317a63151db036cac5ebc8be2.png)

#### Liên kết

*   [](https://www.facebook.com/viblo.asia/)
*   [](https://github.com/viblo-asia/)
*   [](https://chrome.google.com/webstore/detail/viblos-news-feed/mliahmjgdpkkicelofhbhgiidgljijmj)
*   [![Atom Icon](/images/atom-editor.svg)](https://atom.io/packages/viblo)

* * *

© 2025 **Viblo**. All rights reserved.

*   [Về chúng tôi](https://about.viblo.asia/)
*   [Phản hồi](/feedback)
*   [Giúp đỡ](/helps)
*   [FAQs](/faq)
*   [RSS](/rss-channels)
*   [Điều khoản](/terms/vi_term)
*   [![DMCA.com Protection Status](https://images.dmca.com/Badges/dmca-badge-w100-5x1-07.png?ID=41818fcd-5a60-4504-867a-38fde606354e)](https://www.dmca.com/Protection/Status.aspx?ID=41818fcd-5a60-4504-867a-38fde606354e&refurl=https://viblo.asia/p/lam-quen-voi-python-part-2-python-package-module-1VgZvMj9KAw "DMCA.com Protection Status")

[](javascript:void\(0\);)