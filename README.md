# LMSonLesson

 私たちのWebアプリ（LMS on, LMS on Lesson, LMS on Examination）は、無駄を省き、シンプルなつくりであることが特徴で、必要最低限の機能のみを実装しており、使いやすさと効率性を追求しています。
 LMSonLessonは、試験部分を取り除き、講義のみに特化したアプリです
 保守マニュアル、就業規則、研修、等々の構築に最適です

# 公式サイト

https://lmson.net/

# 動作環境

    Python : 3.9以上
    mariaDB: 10.4以上
    Django : 4.2以上

# インストール方法
<ol>
      <li class="py-2">django-admin startproject LMSonLesson</li>
      <li class="py-2">Githubから、ソースコードを取得</li>
      <li class="py-2">pip install -r requirements.txt</li>
      <li class="py-2">~core/settings/develop.pyのDB、logのパラメーターをセット</li>
      <li class="py-2">python manage.py makemigrations</li>
      <li class="py-2">python manage.py migrate</li>
      <li class="py-2">python manage.py createsuperuser</li>
      <li class="py-2">python manage.py runserver</li>
    </ol>


# License

MIT License
Copyright (c) 2023 TABATA,Hitoshi
