# Generated by Django 3.2.8 on 2021-11-05 01:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('languages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languagespecifier',
            name='afrikaans',
            field=models.ManyToManyField(blank=True, null=True, related_name='afrikaans', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='albanian',
            field=models.ManyToManyField(blank=True, null=True, related_name='albanian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='amharic',
            field=models.ManyToManyField(blank=True, null=True, related_name='amharic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='arabic',
            field=models.ManyToManyField(blank=True, null=True, related_name='arabic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='armenian',
            field=models.ManyToManyField(blank=True, null=True, related_name='armenian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='azerbaijani',
            field=models.ManyToManyField(blank=True, null=True, related_name='azerbaijani', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='basque',
            field=models.ManyToManyField(blank=True, null=True, related_name='basque', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='belarusian',
            field=models.ManyToManyField(blank=True, null=True, related_name='belarusian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='bengali',
            field=models.ManyToManyField(blank=True, null=True, related_name='bengali', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='bosnian',
            field=models.ManyToManyField(blank=True, null=True, related_name='bosnian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='bulgarian',
            field=models.ManyToManyField(blank=True, null=True, related_name='bulgarian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='catalan',
            field=models.ManyToManyField(blank=True, null=True, related_name='catalan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='cebuano',
            field=models.ManyToManyField(blank=True, null=True, related_name='cebuano', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='chewa',
            field=models.ManyToManyField(blank=True, null=True, related_name='chewa', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='chinese_Traditional',
            field=models.ManyToManyField(blank=True, null=True, related_name='chinese_Traditional', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='chinese_simplified',
            field=models.ManyToManyField(blank=True, null=True, related_name='chinese_simplified', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='corsican',
            field=models.ManyToManyField(blank=True, null=True, related_name='corsican', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='croatian',
            field=models.ManyToManyField(blank=True, null=True, related_name='croatian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='czech',
            field=models.ManyToManyField(blank=True, null=True, related_name='czech', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='danish',
            field=models.ManyToManyField(blank=True, null=True, related_name='danish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='dutch',
            field=models.ManyToManyField(blank=True, null=True, related_name='dutch', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='english',
            field=models.ManyToManyField(blank=True, null=True, related_name='english', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='esperanto',
            field=models.ManyToManyField(blank=True, null=True, related_name='esperanto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='estonian',
            field=models.ManyToManyField(blank=True, null=True, related_name='estonian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='filipino_tagalog',
            field=models.ManyToManyField(blank=True, null=True, related_name='filipino_tagalog', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='finnish',
            field=models.ManyToManyField(blank=True, null=True, related_name='finnish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='french',
            field=models.ManyToManyField(blank=True, null=True, related_name='french', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='frisian',
            field=models.ManyToManyField(blank=True, null=True, related_name='frisian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='galician',
            field=models.ManyToManyField(blank=True, null=True, related_name='galician', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='georgian',
            field=models.ManyToManyField(blank=True, null=True, related_name='georgian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='german',
            field=models.ManyToManyField(blank=True, null=True, related_name='german', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='greek',
            field=models.ManyToManyField(blank=True, null=True, related_name='greek', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='gujarati',
            field=models.ManyToManyField(blank=True, null=True, related_name='gujarati', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='haitian_creole',
            field=models.ManyToManyField(blank=True, null=True, related_name='haitian_creole', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='hausa',
            field=models.ManyToManyField(blank=True, null=True, related_name='hausa', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='hawaiian',
            field=models.ManyToManyField(blank=True, null=True, related_name='hawaiian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='hebrew',
            field=models.ManyToManyField(blank=True, null=True, related_name='hebrew', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='hindi',
            field=models.ManyToManyField(blank=True, null=True, related_name='hindi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='hmong',
            field=models.ManyToManyField(blank=True, null=True, related_name='hmong', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='hungarian',
            field=models.ManyToManyField(blank=True, null=True, related_name='hungarian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='icelandic',
            field=models.ManyToManyField(blank=True, null=True, related_name='icelandic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='igbo',
            field=models.ManyToManyField(blank=True, null=True, related_name='igbo', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='indonesian',
            field=models.ManyToManyField(blank=True, null=True, related_name='indonesian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='irish',
            field=models.ManyToManyField(blank=True, null=True, related_name='irish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='italian',
            field=models.ManyToManyField(blank=True, null=True, related_name='italian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='japanese',
            field=models.ManyToManyField(blank=True, null=True, related_name='japanese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='javanese',
            field=models.ManyToManyField(blank=True, null=True, related_name='javanese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='kannada',
            field=models.ManyToManyField(blank=True, null=True, related_name='kannada', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='kazakh',
            field=models.ManyToManyField(blank=True, null=True, related_name='kazakh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='khmer',
            field=models.ManyToManyField(blank=True, null=True, related_name='khmer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='kinyarwanda',
            field=models.ManyToManyField(blank=True, null=True, related_name='kinyarwanda', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='korean',
            field=models.ManyToManyField(blank=True, null=True, related_name='korean', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='kurdish_Kurmanji',
            field=models.ManyToManyField(blank=True, null=True, related_name='kurdish_Kurmanji', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='kyrgyz',
            field=models.ManyToManyField(blank=True, null=True, related_name='kyrgyz', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='lao',
            field=models.ManyToManyField(blank=True, null=True, related_name='lao', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='latin',
            field=models.ManyToManyField(blank=True, null=True, related_name='latin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='latvian',
            field=models.ManyToManyField(blank=True, null=True, related_name='latvian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='lithuanian',
            field=models.ManyToManyField(blank=True, null=True, related_name='lithuanian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='luxembourgish',
            field=models.ManyToManyField(blank=True, null=True, related_name='luxembourgish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='macedonian',
            field=models.ManyToManyField(blank=True, null=True, related_name='macedonian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='malagasy',
            field=models.ManyToManyField(blank=True, null=True, related_name='malagasy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='malay',
            field=models.ManyToManyField(blank=True, null=True, related_name='malay', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='malayalam',
            field=models.ManyToManyField(blank=True, null=True, related_name='malayalam', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='maltese',
            field=models.ManyToManyField(blank=True, null=True, related_name='maltese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='maori',
            field=models.ManyToManyField(blank=True, null=True, related_name='maori', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='marathi',
            field=models.ManyToManyField(blank=True, null=True, related_name='marathi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='mongolian',
            field=models.ManyToManyField(blank=True, null=True, related_name='mongolian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='myanmar_burmese',
            field=models.ManyToManyField(blank=True, null=True, related_name='myanmar_burmese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='nepali',
            field=models.ManyToManyField(blank=True, null=True, related_name='nepali', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='norwegian_bokmal',
            field=models.ManyToManyField(blank=True, null=True, related_name='norwegian_bokmal', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='odia',
            field=models.ManyToManyField(blank=True, null=True, related_name='odia', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='pashto',
            field=models.ManyToManyField(blank=True, null=True, related_name='pashto', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='persian',
            field=models.ManyToManyField(blank=True, null=True, related_name='persian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='polish',
            field=models.ManyToManyField(blank=True, null=True, related_name='polish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='portuguese',
            field=models.ManyToManyField(blank=True, null=True, related_name='portuguese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='punjabi_gurmukhi',
            field=models.ManyToManyField(blank=True, null=True, related_name='punjabi_gurmukhi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='romanian',
            field=models.ManyToManyField(blank=True, null=True, related_name='romanian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='russian',
            field=models.ManyToManyField(blank=True, null=True, related_name='russian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='samoan',
            field=models.ManyToManyField(blank=True, null=True, related_name='samoan', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='scottish_gaelic',
            field=models.ManyToManyField(blank=True, null=True, related_name='scottish_gaelic', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='serbian',
            field=models.ManyToManyField(blank=True, null=True, related_name='serbian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='shona',
            field=models.ManyToManyField(blank=True, null=True, related_name='shona', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='sindhi',
            field=models.ManyToManyField(blank=True, null=True, related_name='sindhi', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='sinhala',
            field=models.ManyToManyField(blank=True, null=True, related_name='sinhala', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='slovak',
            field=models.ManyToManyField(blank=True, null=True, related_name='slovak', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='slovenian',
            field=models.ManyToManyField(blank=True, null=True, related_name='slovenian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='somali',
            field=models.ManyToManyField(blank=True, null=True, related_name='somali', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='sotho',
            field=models.ManyToManyField(blank=True, null=True, related_name='sotho', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='spanish',
            field=models.ManyToManyField(blank=True, null=True, related_name='spanish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='sundanese',
            field=models.ManyToManyField(blank=True, null=True, related_name='sundanese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='swahili',
            field=models.ManyToManyField(blank=True, null=True, related_name='swahili', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='swedish',
            field=models.ManyToManyField(blank=True, null=True, related_name='swedish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='tajik',
            field=models.ManyToManyField(blank=True, null=True, related_name='tajik', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='tamil',
            field=models.ManyToManyField(blank=True, null=True, related_name='tamil', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='tatar',
            field=models.ManyToManyField(blank=True, null=True, related_name='tatar', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='telugu',
            field=models.ManyToManyField(blank=True, null=True, related_name='telugu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='thai',
            field=models.ManyToManyField(blank=True, null=True, related_name='thai', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='turkish',
            field=models.ManyToManyField(blank=True, null=True, related_name='turkish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='turkmen',
            field=models.ManyToManyField(blank=True, null=True, related_name='turkmen', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='ukrainian',
            field=models.ManyToManyField(blank=True, null=True, related_name='ukrainian', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='urdu',
            field=models.ManyToManyField(blank=True, null=True, related_name='urdu', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='uyghur',
            field=models.ManyToManyField(blank=True, null=True, related_name='uyghur', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='uzbek',
            field=models.ManyToManyField(blank=True, null=True, related_name='uzbek', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='vietnamese',
            field=models.ManyToManyField(blank=True, null=True, related_name='vietnamese', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='welsh',
            field=models.ManyToManyField(blank=True, null=True, related_name='welsh', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='xhosa',
            field=models.ManyToManyField(blank=True, null=True, related_name='xhosa', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='yiddish',
            field=models.ManyToManyField(blank=True, null=True, related_name='yiddish', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='yoruba',
            field=models.ManyToManyField(blank=True, null=True, related_name='yoruba', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='languagespecifier',
            name='zulu',
            field=models.ManyToManyField(blank=True, null=True, related_name='zulu', to=settings.AUTH_USER_MODEL),
        ),
    ]