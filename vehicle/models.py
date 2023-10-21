from django.db import models
from datetime import datetime

MAKERS = (
    ('レクサス', 'レクサス'),
    ('トヨタ', 'トヨタ'),
    ('日産', '日産'),
    ('ホンダ', 'ホンダ'),
    ('マツダ', 'マツダ'),
    ('スバル', 'スバル'),
    ('スズキ', 'スズキ'),
    ('三菱', '三菱'),
    ('ダイハツ', 'ダイハツ'),
    ('いすゞ', 'いすゞ'),
    ('光岡自動車', '光岡自動車'),
    ('トミーカイラ', 'トミーカイラ'),
    ('日野自動車', '日野自動車'),
    ('UDトラックス', 'UDトラックス'),
    ('三菱ふそう', '三菱ふそう'),
    ('国産車その他', '国産車その他'),
)

MISSION_OPTIONS = (
    ('MT', 'MT'),
    ('AT', 'AT'),
    ('Automanual', 'Automanual'),
    ('CVT', 'CVT'),
    ('Others', 'Others')
)

DRIVE_SYSTEM_OPTIONS = (
    ('FF', 'FF'),
    ('FR', 'FR'),
    ('MR', 'MR'),
    ('RR', 'RR'),
    ('4WD', '4WD'),
)

BODY_TYPE = (
    ('軽自動車', '軽自動車'),
    ('コンパクトカー', 'コンパクトカー'),
    ('ミニバン', 'ミニバン'),
    ('ステーションワゴン', 'ステーションワゴン'),
    ('SUV・クロカン', 'SUV・クロカン'),
    ('セダン', 'セダン'),
    ('クーペ', 'クーペ'),
    ('オープンカー', 'オープンカー'),
    ('ハイブリッド', 'ハイブリッド'),
    ('キャンピングカー', 'キャンピングカー'),
    ('ハッチバック', 'ハッチバック'),
    ('ピックアップトラック', 'ピックアップトラック'),
    ('商用車・バン', '商用車・バン'),
    ('トラック', 'トラック'),
    ('その他', 'その他'),

)

REGION_OPTIONS = (
    ('北海道', '北海道'),
    ('青森県', '青森県'),
    ('岩手県', '岩手県'),
    ('宮城県', '宮城県'),
    ('秋田県', '秋田県'),
    ('山形県', '山形県'),
    ('福島県', '福島県'),
    ('茨城県', '茨城県'),
    ('栃木県', '栃木県'),
    ('群馬県', '群馬県'),
    ('埼玉県', '埼玉県'),
    ('千葉県', '千葉県'),
    ('東京都', '東京都'),
    ('神奈川県', '神奈川県'),
    ('新潟県', '新潟県'),
    ('富山県', '富山県'),
    ('石川県', '石川県'),
    ('福井県', '福井県'),
    ('山梨県', '山梨県'),
    ('長野県', '長野県'),
    ('岐阜県', '岐阜県'),
    ('静岡県', '静岡県'),
    ('愛知県', '愛知県'),
    ('三重県', '三重県'),
    ('滋賀県', '滋賀県'),
    ('京都府', '京都府'),
    ('大阪府', '大阪府'),
    ('兵庫県', '兵庫県'),
    ('奈良県', '奈良県'),
    ('和歌山県', '和歌山県'),
    ('鳥取県', '鳥取県'),
    ('島根県', '島根県'),
    ('岡山県', '岡山県'),
    ('広島県', '広島県'),
    ('山口県', '山口県'),
    ('徳島県', '徳島県'),
    ('香川県', '香川県'),
    ('愛媛県', '愛媛県'),
    ('高知県', '高知県'),
    ('福岡県', '福岡県'),
    ('佐賀県', '佐賀県'),
    ('長崎県', '長崎県'),
    ('熊本県', '熊本県'),
    ('大分県', '大分県'),
    ('宮崎県', '宮崎県'),
    ('鹿児島県', '鹿児島県'),
    ('沖縄県', '沖縄県'),
)

OWNER_RECORD = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
    ('11以上', '11以上'),
)

REPAIRS = (
    ('修理歴なし', '修理歴なし'),
    ('修理歴あり', '修理歴あり')
)

STATUS_ITEMS = (
    ('販売中', '販売中'),
    ('交渉中', '交渉中'),
    ('成約済み', '成約済み')
)


class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    model_num = models.CharField(max_length=120, verbose_name='モデル番号')
    name = models.CharField(max_length=120, verbose_name="車名")
    maker = models.CharField(choices=MAKERS, max_length=120, verbose_name='メーカー')
    region = models.CharField(choices=REGION_OPTIONS, max_length=100, verbose_name='地域')
    transmission = models.CharField(choices=MISSION_OPTIONS, max_length=100, verbose_name='ミッション')
    drive_system = models.CharField(choices=DRIVE_SYSTEM_OPTIONS, max_length=100, verbose_name='駆動方式')
    body_type = models.CharField(choices=BODY_TYPE, max_length=120, verbose_name='ボディータイプ')
    body_color = models.CharField(max_length=120, verbose_name='ボディーカラー')
    price = models.IntegerField(verbose_name='価格')
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='車輌画像')
    car_age = models.CharField(max_length=120, verbose_name='年式')
    owner = models.CharField(choices=OWNER_RECORD, max_length=120, verbose_name='オーナー')
    repair_record = models.CharField(choices=REPAIRS, max_length=100, verbose_name='修理歴')
    smoking_record = models.BooleanField(default=False, verbose_name='禁煙車輌')
    vin = models.CharField(max_length=120, blank=True, verbose_name='VIN番号')
    frame_num = models.CharField(max_length=120, blank=True, verbose_name='フレーム番号')
    status = models.CharField(choices=STATUS_ITEMS, max_length=100, default=0, verbose_name='販売状況')
    is_published = models.BooleanField(default=False, verbose_name='公開する')
    list_date = models.DateTimeField(default=datetime.now, blank=True, editable=False)

    def __str__(self):
        return f"Vehicle:{self.name}"

    class Meta:
        verbose_name = "車輌データ"
        verbose_name_plural = verbose_name


