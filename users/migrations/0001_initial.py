# Generated by Django 3.2.5 on 2021-07-29 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models
import users.models.user


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nome')),
                ('last_name', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-mail')),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14, verbose_name='CPF')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Número de celular')),
                ('receive_future_promotional_emails', models.BooleanField(default=False, help_text='Caso seja falso, não enviar emails pro usuário', verbose_name='Receber promoções futuras por email')),
                ('provide_data_to_improve_user_exp', models.BooleanField(default=False, help_text='Caso seja falso, não usar dados do usuário', verbose_name='Fornecer dados para melhorar a experiência')),
                ('is_staff', models.BooleanField(default=False, help_text='Define se o usuário tem acesso ao admin', verbose_name='Membro da equipe')),
                ('is_active', models.BooleanField(default=False, help_text='Define se o usuário ativou a conta no email', verbose_name='Ativo')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Criação')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', users.models.user.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='VerifyEmailToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PasswordResetToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=64, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100, verbose_name='País')),
                ('state', localflavor.br.models.BRStateField(max_length=2, verbose_name='Estado')),
                ('postal_code', localflavor.br.models.BRPostalCodeField(max_length=9, verbose_name='CEP')),
                ('city', models.CharField(max_length=100, verbose_name='Cidade')),
                ('district', models.CharField(max_length=100, verbose_name='Bairro')),
                ('street', models.CharField(max_length=100, verbose_name='Rua')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('complement', models.CharField(blank=True, max_length=100, null=True, verbose_name='Complemento')),
                ('owner', models.ForeignKey(help_text='Usuário dono do endereço', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Endereço',
                'verbose_name_plural': 'Endereços',
            },
        ),
    ]
