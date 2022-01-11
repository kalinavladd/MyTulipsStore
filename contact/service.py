from django.core.mail import send_mail


def send(user_mail):
    send_mail(
        f"ВАМ ПИЗДА {user_mail}, Ваше лаве ушло в пизду",
        "Мы будем присылать вам шляпу от КАЛИНЫ",
        "phantomassassinkill@gmail.com",
        [user_mail],
        fail_silently=False,

    )
