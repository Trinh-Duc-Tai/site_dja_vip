# Generated by Django 5.0 on 2023-12-29 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leeon_voiceotp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opttopup',
            options={'managed': False, 'verbose_name_plural': 'OptTopup'},
        ),
        migrations.AlterModelOptions(
            name='otpcallpartner202312',
            options={'managed': False, 'verbose_name_plural': 'OtpCallPartner202312'},
        ),
        migrations.AlterModelOptions(
            name='otpcallpartner202401',
            options={'managed': False, 'verbose_name_plural': 'OtpCallPartner202401'},
        ),
        migrations.AlterModelOptions(
            name='otpcallvendor202312',
            options={'managed': False, 'verbose_name_plural': 'OtpCallVendor202312'},
        ),
        migrations.AlterModelOptions(
            name='otpcallvendor202401',
            options={'managed': False, 'verbose_name_plural': 'OtpCallVendor202401'},
        ),
        migrations.AlterModelOptions(
            name='otppartner',
            options={'managed': False, 'verbose_name_plural': 'OtpPartner'},
        ),
        migrations.AlterModelOptions(
            name='otpvendor',
            options={'managed': False, 'verbose_name_plural': 'OtpVendor'},
        ),
        migrations.AlterModelOptions(
            name='prefixtelco',
            options={'managed': False, 'verbose_name_plural': 'PrefixTelco'},
        ),
        migrations.AlterModelOptions(
            name='tmp',
            options={'managed': False, 'verbose_name_plural': 'Tmp'},
        ),
    ]