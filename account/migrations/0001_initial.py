# Generated by Django 5.0.6 on 2024-06-12 13:19

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("account_type", models.CharField(max_length=255)),
                (
                    "balance",
                    models.DecimalField(decimal_places=2, default=0, max_digits=10),
                ),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("AED", "United Arab Emirates Dirham"),
                            ("AFN", "Afghan Afghani"),
                            ("ALL", "Albanian Lek"),
                            ("AMD", "Armenian Dram"),
                            ("ANG", "Netherlands Antillean Guilder"),
                            ("AOA", "Angolan Kwanza"),
                            ("ARS", "Argentine Peso"),
                            ("AUD", "Australian Dollar"),
                            ("AWG", "Aruban Florin"),
                            ("AZN", "Azerbaijani Manat"),
                            ("BAM", "Bosnia-Herzegovina Convertible Mark"),
                            ("BBD", "Barbadian Dollar"),
                            ("BDT", "Bangladeshi Taka"),
                            ("BGN", "Bulgarian Lev"),
                            ("BHD", "Bahraini Dinar"),
                            ("BIF", "Burundian Franc"),
                            ("BMD", "Bermudian Dollar"),
                            ("BND", "Brunei Dollar"),
                            ("BOB", "Bolivian Boliviano"),
                            ("BRL", "Brazilian Real"),
                            ("BSD", "Bahamian Dollar"),
                            ("BTN", "Bhutanese Ngultrum"),
                            ("BWP", "Botswana Pula"),
                            ("BYN", "Belarusian Ruble"),
                            ("BZD", "Belize Dollar"),
                            ("CAD", "Canadian Dollar"),
                            ("CDF", "Congolese Franc"),
                            ("CHF", "Swiss Franc"),
                            ("CLP", "Chilean Peso"),
                            ("CNY", "Chinese Yuan"),
                            ("COP", "Colombian Peso"),
                            ("CRC", "Costa Rican Colón"),
                            ("CUP", "Cuban Peso"),
                            ("CVE", "Cape Verdean Escudo"),
                            ("CZK", "Czech Koruna"),
                            ("DJF", "Djiboutian Franc"),
                            ("DKK", "Danish Krone"),
                            ("DOP", "Dominican Peso"),
                            ("DZD", "Algerian Dinar"),
                            ("EGP", "Egyptian Pound"),
                            ("ERN", "Eritrean Nakfa"),
                            ("ETB", "Ethiopian Birr"),
                            ("EUR", "Euro"),
                            ("FJD", "Fijian Dollar"),
                            ("FKP", "Falkland Islands Pound"),
                            ("FOK", "Faroese Króna"),
                            ("GBP", "British Pound Sterling"),
                            ("GEL", "Georgian Lari"),
                            ("GGP", "Guernsey Pound"),
                            ("GHS", "Ghanaian Cedi"),
                            ("GIP", "Gibraltar Pound"),
                            ("GMD", "Gambian Dalasi"),
                            ("GNF", "Guinean Franc"),
                            ("GTQ", "Guatemalan Quetzal"),
                            ("GYD", "Guyanese Dollar"),
                            ("HKD", "Hong Kong Dollar"),
                            ("HNL", "Honduran Lempira"),
                            ("HRK", "Croatian Kuna"),
                            ("HTG", "Haitian Gourde"),
                            ("HUF", "Hungarian Forint"),
                            ("IDR", "Indonesian Rupiah"),
                            ("ILS", "Israeli New Shekel"),
                            ("IMP", "Isle of Man Pound"),
                            ("INR", "Indian Rupee"),
                            ("IQD", "Iraqi Dinar"),
                            ("IRR", "Iranian Rial"),
                            ("ISK", "Icelandic Króna"),
                            ("JEP", "Jersey Pound"),
                            ("JMD", "Jamaican Dollar"),
                            ("JOD", "Jordanian Dinar"),
                            ("JPY", "Japanese Yen"),
                            ("KES", "Kenyan Shilling"),
                            ("KGS", "Kyrgyzstani Som"),
                            ("KHR", "Cambodian Riel"),
                            ("KID", "Kiribati Dollar"),
                            ("KMF", "Comorian Franc"),
                            ("KRW", "South Korean Won"),
                            ("KWD", "Kuwaiti Dinar"),
                            ("KYD", "Cayman Islands Dollar"),
                            ("KZT", "Kazakhstani Tenge"),
                            ("LAK", "Lao Kip"),
                            ("LBP", "Lebanese Pound"),
                            ("LKR", "Sri Lankan Rupee"),
                            ("LRD", "Liberian Dollar"),
                            ("LSL", "Lesotho Loti"),
                            ("LYD", "Libyan Dinar"),
                            ("MAD", "Moroccan Dirham"),
                            ("MDL", "Moldovan Leu"),
                            ("MGA", "Malagasy Ariary"),
                            ("MKD", "Macedonian Denar"),
                            ("MMK", "Myanmar Kyat"),
                            ("MNT", "Mongolian Tögrög"),
                            ("MOP", "Macanese Pataca"),
                            ("MRU", "Mauritanian Ouguiya"),
                            ("MUR", "Mauritian Rupee"),
                            ("MVR", "Maldivian Rufiyaa"),
                            ("MWK", "Malawian Kwacha"),
                            ("MXN", "Mexican Peso"),
                            ("MYR", "Malaysian Ringgit"),
                            ("MZN", "Mozambican Metical"),
                            ("NAD", "Namibian Dollar"),
                            ("NGN", "Nigerian Naira"),
                            ("NIO", "Nicaraguan Córdoba"),
                            ("NOK", "Norwegian Krone"),
                            ("NPR", "Nepalese Rupee"),
                            ("NZD", "New Zealand Dollar"),
                            ("OMR", "Omani Rial"),
                            ("PAB", "Panamanian Balboa"),
                            ("PEN", "Peruvian Sol"),
                            ("PGK", "Papua New Guinean Kina"),
                            ("PHP", "Philippine Peso"),
                            ("PKR", "Pakistani Rupee"),
                            ("PLN", "Polish Złoty"),
                            ("PYG", "Paraguayan Guaraní"),
                            ("QAR", "Qatari Riyal"),
                            ("RON", "Romanian Leu"),
                            ("RSD", "Serbian Dinar"),
                            ("RUB", "Russian Ruble"),
                            ("RWF", "Rwandan Franc"),
                            ("SAR", "Saudi Riyal"),
                            ("SBD", "Solomon Islands Dollar"),
                            ("SCR", "Seychellois Rupee"),
                            ("SDG", "Sudanese Pound"),
                            ("SEK", "Swedish Krona"),
                            ("SGD", "Singapore Dollar"),
                            ("SHP", "Saint Helena Pound"),
                            ("SLL", "Sierra Leonean Leone"),
                            ("SOS", "Somali Shilling"),
                            ("SRD", "Surinamese Dollar"),
                            ("SSP", "South Sudanese Pound"),
                            ("STN", "São Tomé and Príncipe Dobra"),
                            ("SYP", "Syrian Pound"),
                            ("SZL", "Eswatini Lilangeni"),
                            ("THB", "Thai Baht"),
                            ("TJS", "Tajikistani Somoni"),
                            ("TMT", "Turkmenistani Manat"),
                            ("TND", "Tunisian Dinar"),
                            ("TOP", "Tongan Paʻanga"),
                            ("TRY", "Turkish Lira"),
                            ("TTD", "Trinidad and Tobago Dollar"),
                            ("TVD", "Tuvaluan Dollar"),
                            ("TWD", "New Taiwan Dollar"),
                            ("TZS", "Tanzanian Shilling"),
                            ("UAH", "Ukrainian Hryvnia"),
                            ("UGX", "Ugandan Shilling"),
                            ("USD", "United States Dollar"),
                            ("UYU", "Uruguayan Peso"),
                            ("UZS", "Uzbekistani Som"),
                            ("VES", "Venezuelan Bolívar"),
                            ("VND", "Vietnamese Đồng"),
                            ("VUV", "Vanuatu Vatu"),
                            ("WST", "Samoan Tālā"),
                            ("XAF", "Central African CFA Franc"),
                            ("XCD", "East Caribbean Dollar"),
                            ("XOF", "West African CFA Franc"),
                            ("XPF", "CFP Franc"),
                            ("YER", "Yemeni Rial"),
                            ("ZAR", "South African Rand"),
                            ("ZMW", "Zambian Kwacha"),
                            ("ZWL", "Zimbabwean Dollar"),
                        ],
                        max_length=3,
                    ),
                ),
                (
                    "conversion_rate",
                    models.DecimalField(decimal_places=4, max_digits=10),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Currency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "main_currency",
                    models.CharField(
                        choices=[
                            ("AED", "United Arab Emirates Dirham"),
                            ("AFN", "Afghan Afghani"),
                            ("ALL", "Albanian Lek"),
                            ("AMD", "Armenian Dram"),
                            ("ANG", "Netherlands Antillean Guilder"),
                            ("AOA", "Angolan Kwanza"),
                            ("ARS", "Argentine Peso"),
                            ("AUD", "Australian Dollar"),
                            ("AWG", "Aruban Florin"),
                            ("AZN", "Azerbaijani Manat"),
                            ("BAM", "Bosnia-Herzegovina Convertible Mark"),
                            ("BBD", "Barbadian Dollar"),
                            ("BDT", "Bangladeshi Taka"),
                            ("BGN", "Bulgarian Lev"),
                            ("BHD", "Bahraini Dinar"),
                            ("BIF", "Burundian Franc"),
                            ("BMD", "Bermudian Dollar"),
                            ("BND", "Brunei Dollar"),
                            ("BOB", "Bolivian Boliviano"),
                            ("BRL", "Brazilian Real"),
                            ("BSD", "Bahamian Dollar"),
                            ("BTN", "Bhutanese Ngultrum"),
                            ("BWP", "Botswana Pula"),
                            ("BYN", "Belarusian Ruble"),
                            ("BZD", "Belize Dollar"),
                            ("CAD", "Canadian Dollar"),
                            ("CDF", "Congolese Franc"),
                            ("CHF", "Swiss Franc"),
                            ("CLP", "Chilean Peso"),
                            ("CNY", "Chinese Yuan"),
                            ("COP", "Colombian Peso"),
                            ("CRC", "Costa Rican Colón"),
                            ("CUP", "Cuban Peso"),
                            ("CVE", "Cape Verdean Escudo"),
                            ("CZK", "Czech Koruna"),
                            ("DJF", "Djiboutian Franc"),
                            ("DKK", "Danish Krone"),
                            ("DOP", "Dominican Peso"),
                            ("DZD", "Algerian Dinar"),
                            ("EGP", "Egyptian Pound"),
                            ("ERN", "Eritrean Nakfa"),
                            ("ETB", "Ethiopian Birr"),
                            ("EUR", "Euro"),
                            ("FJD", "Fijian Dollar"),
                            ("FKP", "Falkland Islands Pound"),
                            ("FOK", "Faroese Króna"),
                            ("GBP", "British Pound Sterling"),
                            ("GEL", "Georgian Lari"),
                            ("GGP", "Guernsey Pound"),
                            ("GHS", "Ghanaian Cedi"),
                            ("GIP", "Gibraltar Pound"),
                            ("GMD", "Gambian Dalasi"),
                            ("GNF", "Guinean Franc"),
                            ("GTQ", "Guatemalan Quetzal"),
                            ("GYD", "Guyanese Dollar"),
                            ("HKD", "Hong Kong Dollar"),
                            ("HNL", "Honduran Lempira"),
                            ("HRK", "Croatian Kuna"),
                            ("HTG", "Haitian Gourde"),
                            ("HUF", "Hungarian Forint"),
                            ("IDR", "Indonesian Rupiah"),
                            ("ILS", "Israeli New Shekel"),
                            ("IMP", "Isle of Man Pound"),
                            ("INR", "Indian Rupee"),
                            ("IQD", "Iraqi Dinar"),
                            ("IRR", "Iranian Rial"),
                            ("ISK", "Icelandic Króna"),
                            ("JEP", "Jersey Pound"),
                            ("JMD", "Jamaican Dollar"),
                            ("JOD", "Jordanian Dinar"),
                            ("JPY", "Japanese Yen"),
                            ("KES", "Kenyan Shilling"),
                            ("KGS", "Kyrgyzstani Som"),
                            ("KHR", "Cambodian Riel"),
                            ("KID", "Kiribati Dollar"),
                            ("KMF", "Comorian Franc"),
                            ("KRW", "South Korean Won"),
                            ("KWD", "Kuwaiti Dinar"),
                            ("KYD", "Cayman Islands Dollar"),
                            ("KZT", "Kazakhstani Tenge"),
                            ("LAK", "Lao Kip"),
                            ("LBP", "Lebanese Pound"),
                            ("LKR", "Sri Lankan Rupee"),
                            ("LRD", "Liberian Dollar"),
                            ("LSL", "Lesotho Loti"),
                            ("LYD", "Libyan Dinar"),
                            ("MAD", "Moroccan Dirham"),
                            ("MDL", "Moldovan Leu"),
                            ("MGA", "Malagasy Ariary"),
                            ("MKD", "Macedonian Denar"),
                            ("MMK", "Myanmar Kyat"),
                            ("MNT", "Mongolian Tögrög"),
                            ("MOP", "Macanese Pataca"),
                            ("MRU", "Mauritanian Ouguiya"),
                            ("MUR", "Mauritian Rupee"),
                            ("MVR", "Maldivian Rufiyaa"),
                            ("MWK", "Malawian Kwacha"),
                            ("MXN", "Mexican Peso"),
                            ("MYR", "Malaysian Ringgit"),
                            ("MZN", "Mozambican Metical"),
                            ("NAD", "Namibian Dollar"),
                            ("NGN", "Nigerian Naira"),
                            ("NIO", "Nicaraguan Córdoba"),
                            ("NOK", "Norwegian Krone"),
                            ("NPR", "Nepalese Rupee"),
                            ("NZD", "New Zealand Dollar"),
                            ("OMR", "Omani Rial"),
                            ("PAB", "Panamanian Balboa"),
                            ("PEN", "Peruvian Sol"),
                            ("PGK", "Papua New Guinean Kina"),
                            ("PHP", "Philippine Peso"),
                            ("PKR", "Pakistani Rupee"),
                            ("PLN", "Polish Złoty"),
                            ("PYG", "Paraguayan Guaraní"),
                            ("QAR", "Qatari Riyal"),
                            ("RON", "Romanian Leu"),
                            ("RSD", "Serbian Dinar"),
                            ("RUB", "Russian Ruble"),
                            ("RWF", "Rwandan Franc"),
                            ("SAR", "Saudi Riyal"),
                            ("SBD", "Solomon Islands Dollar"),
                            ("SCR", "Seychellois Rupee"),
                            ("SDG", "Sudanese Pound"),
                            ("SEK", "Swedish Krona"),
                            ("SGD", "Singapore Dollar"),
                            ("SHP", "Saint Helena Pound"),
                            ("SLL", "Sierra Leonean Leone"),
                            ("SOS", "Somali Shilling"),
                            ("SRD", "Surinamese Dollar"),
                            ("SSP", "South Sudanese Pound"),
                            ("STN", "São Tomé and Príncipe Dobra"),
                            ("SYP", "Syrian Pound"),
                            ("SZL", "Eswatini Lilangeni"),
                            ("THB", "Thai Baht"),
                            ("TJS", "Tajikistani Somoni"),
                            ("TMT", "Turkmenistani Manat"),
                            ("TND", "Tunisian Dinar"),
                            ("TOP", "Tongan Paʻanga"),
                            ("TRY", "Turkish Lira"),
                            ("TTD", "Trinidad and Tobago Dollar"),
                            ("TVD", "Tuvaluan Dollar"),
                            ("TWD", "New Taiwan Dollar"),
                            ("TZS", "Tanzanian Shilling"),
                            ("UAH", "Ukrainian Hryvnia"),
                            ("UGX", "Ugandan Shilling"),
                            ("USD", "United States Dollar"),
                            ("UYU", "Uruguayan Peso"),
                            ("UZS", "Uzbekistani Som"),
                            ("VES", "Venezuelan Bolívar"),
                            ("VND", "Vietnamese Đồng"),
                            ("VUV", "Vanuatu Vatu"),
                            ("WST", "Samoan Tālā"),
                            ("XAF", "Central African CFA Franc"),
                            ("XCD", "East Caribbean Dollar"),
                            ("XOF", "West African CFA Franc"),
                            ("XPF", "CFP Franc"),
                            ("YER", "Yemeni Rial"),
                            ("ZAR", "South African Rand"),
                            ("ZMW", "Zambian Kwacha"),
                            ("ZWL", "Zimbabwean Dollar"),
                        ],
                        max_length=3,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
