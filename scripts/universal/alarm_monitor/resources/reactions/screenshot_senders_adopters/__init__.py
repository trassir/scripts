# AdoptedSender - abstract class
# Задача потомков создавать адаптеры к различным
# сендерам для отправки скриншотов.

from screenshot_senders_adopters import AdoptedEmailSender
from screenshot_senders_adopters import AdoptedTelegramSender
from screenshot_senders_adopters import AdoptedFTPSender
from screenshot_senders_adopters import FireAlarm


