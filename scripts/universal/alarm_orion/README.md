## Основные функции
Скрипт позволяет ассоциировать один или более каналов для датчика Orion  с последующим выводом каналов на тревожный монитор при сработке на событие.

## Установка
* Добавить скрипт в разделе Автоматизация->Новый скрипт->Загрузить пример->Из файла.
* После загрузки скрипта необходимо нажать на кнопку «Сохранить, запустить».
* Выключить скрипт, сняв чек-бокс и выполнить его настройку.
* После выбора нужных реакций и тревог, включить скрипт.

## Настройка скрипта
<img src="settings.png" alt="settings.png" align=left>

1. Выбрать сервер к которому подключен Orion
2. Выбрать основной монитор для отображения
3. Выбрать шаблон после тревоги
4. Указать таймаут до сброса тревоги( в секундах)
5. Указать задержку на повторную реакцию на событие от датчика(в секундах)
6. Указать через "," события на которые будет реагировать скрипт(без кавычек)

<img src="settings1.png" alt="settings1.png" align=left>

1. Выбрать датчик orion
2. Выбрать канал для ассоциации с датчиком

## Список событий Orion

```
{
    "Орион": {
        "Орион отключен": "Orion Disconnected",
        "Орион подключен": "Orion Connected"
    },
    "Реле Орион": {
        "Включение реле": "ON",
        "Восстановление зоны контроля взлома": "Key Break Restored",
        "Восстановление цепи выхода": "Ok",
        "Выключение реле": "OFF",
        "Изменение состояние выхода": "Out State Changed",
        "Короткое замыкание выхода": "Key Short Circuit",
        "Обрыв цепи выхода": "Wire Cut",
        "Отказ цепи пуска": "Start Chain Fault",
        "Отключение выхода": "Disconnect",
        "Подключение выхода": "Connect",
        "Пуск РО": "RO Start",
        "Реле мигает %1": "Blink %1",
        "Сброс пуска РО": "RO Reset",
        "Срабатывание цепи пуска": "Start Chain Works",
        "Тревога взлома": "Key Break Alert"
    },
    "Считыватель Орион": {
        "Access Granted (by bytton)": "Access Granted (by button)",
        "Восстановление доступа": "Allowed Access By Key",
        "Восстановление целостности двери": "Door Restored",
        "Дверь взломана": "Door Broken",
        "Дверь заблокирована": "Door Blocked",
        "Доступ закрыт": "No Access To All",
        "Доступ отклонен %1": "Access Denied %1",
        "Доступ предоставлен %1": "Access Granted %1",
        "Запрет доступа %1": "No Access %1",
        "Нет контакта": "Reader Contact Lost",
        "Проход": "Walk Detected",
        "Свободный доступ открыт": "Free Walk Allowed"
    },
    "Точка доступа": {
        "Доступ отклонён %1 (%2)": "Deny: %1 (%2)",
        "Доступ предоставлен %1 (%2)": "Allow: %1 (%2)",
        "Проход %1 (%2)": "Pass: %1 (%2)",
        "Соединение разорвано": "Access Point Disconnected",
        "Соединение установлено": "Access Point Connected",
        "Точка доступа открыта на один проход": "Access Point Once Opened",
        "Точка Доступа: %1": "Access Point: %1",
        "Тревога: %1 (%2)": "Alarm: %1 (%2)",
        "Установлен режим работы 'закрыто'": "Access Point Closed To All",
        "Установлен режим работы 'открыто'": "Access Point Opened To All",
        "Установлен режим работы 'по ключу'": "Access Point Allows By Key"
    },
    "Устройство Орион": {
        "Авария ДПЛС": "DPLS Alarm",
        "Авария питания": "Device Power Fault",
        "Включение принтера": "Printer On",
        "Включение пульта": "Pult On",
        "Восстановление батареи устройства": "Device Battery Restored",
        "Восстановление ветви": "Branch On",
        "Восстановление внутренней зоны": "Internal Zone Restored",
        "Восстановление ДПЛС": "DPLS Restored",
        "Восстановление зоны контроля взлома устройства": "Device Break Restored",
        "Восстановление контакта": "Contact Restored",
        "Восстановление напряжения питания": "Voltage Restored",
        "Восстановление питания": "Device Power Source Restored",
        "Восстановление питания устройства": "Device Power Restored",
        "Вход в режим программирования": "Вход в режим программирования",
        "Выключение принтера": "Printer Off",
        "Журнал заполнен": "Journal Filled",
        "Журнал переполнен": "Journal Overfilled",
        "Изменение времени": "Time Changed",
        "Изменение даты": "Изменение даты",
        "Короткое замыкание ДПЛС": "DPLS Short Circuit",
        "Локальное программирование": "Local Programming",
        "Метка контроля канала": "Channel Control Mark",
        "Неисправность батареи устройства": "Device Battery Fault",
        "Неисправность источника питания устройства": "Power Source Fail",
        "Неисправность телефонной линии": "Phone Line Fault",
        "Нет контакта с устройством": "Device Contact Lost",
        "Обрыв ДПЛС": "DPLS Fault",
        "Отключение ветви": "Branch Off",
        "Ошибка автоматического теста": "Autotest Failed",
        "Подмена прибора": "Device Was Replaced",
        "Потерян канал": "Channel Lost",
        "Прошел день": "отметка времени:Day Passed Timestamp",
        "Прошел час": "отметка времени:Hour Passed TImestamp",
        "Ручной тест": "Manual Test",
        "Сброс сторожевого таймера": "Timer Reset",
        "Сброс тревоги в зоне охраны": "Zone Alarm Reset",
        "Сброс тревоги уйстройства": "Device Alarm Reset",
        "Тревога взлома уйстройства": "Device Break Alert"
    },
    "Шлейф Орион": {
        "Automation OFF": "Automation OFF",
        "Аварийное повышение уровня": "Alarm: Level High",
        "Аварийное понижение уровня": "Alarm: Level Low",
        "Аварийный пуск": "ASPT Alarmed Start",
        "Авария ЗУ": "ZU Fault",
        "Авария сети 220": "Line Power Fault",
        "Автоматика включена": "Automation ON",
        "Блокировка пуска": "ASPT Start Blocked",
        "Взлом": "Break Alarm",
        "Взят": "Armed",
        "Включение насоса": "Pump ON",
        "Внимание": "Attention",
        "Восстановление батареи": "Line Battery Restored",
        "Восстановление внешней зоны": "External Zone Restore",
        "Восстановление зоны контроля": "Zone Restore",
        "Восстановление ЗУ": "ZU Ok",
        "Восстановление источника питания": "Line Power Source Restored",
        "Восстановление сети 220": "Line Power Restored",
        "Восстановление снятой зоны": "Disarmed Zone Restore",
        "Восстановление техн": "Tech Restore",
        "Выключение выходного напряжения источника": "Power Source Off",
        "Выключение насоса": "Pump OFF",
        "Выключение пожарного тестирования": "Fire Test Off",
        "Задержка взятия": "Arm Delayed",
        "Задержка пуска АСПТ": "ASPT Start Dlayed",
        "Идет взятие...": "Arming...",
        "Идет снятие...": "Disasrming...",
        "Контакт потерян": "Line Contact Lost",
        "Короткое замыкание": "Line Short Circuit",
        "Нарешение 2 техн. ШС": "Tech 2 Fault",
        "Нарушение снятой зоны": "Disarmed Zone Fault",
        "Нарушение техн": "Tech Fault",
        "Невзятие": "Not Armed",
        "Неисправность батареи": "Line Battery Fault",
        "Неисправность источника питания": "Power Source Fault",
        "Неисправность термометра": "Thermometer Broken",
        "Некорректный ответ": "Incorrect Answer",
        "Неудачный пуск": "Unsuccessful start",
        "Неустойчивый ответ": "Unstable Answer",
        "Обрыв шлейфа": "Cut",
        "Отказ СДУ": "SDU Fault",
        "Отключен": "Disconnected",
        "Отмена пуска АСПТ": "ASPT Start Cancelled",
        "Ошибка параметров ШС": "Params Error",
        "Перегрузка источника питания": "Power Source Overload",
        "Перегрузка источника устранена": "Power Source Normal",
        "Повышение температуры": "Temperature High",
        "Повышение уровня": "Level Hight",
        "Подключен": "Connected",
        "Подключение выходного напряжения источника питания": "Power Source On",
        "Пожар": "Fire",
        "Пожарное оборуд в норме": "Fire Device Ok",
        "Пожарное оборудов неисправно": "Fire Device Fault",
        "Пожарное тестирование": "Fire Test",
        "Понижение температуры": "Temperature Low",
        "Понижение уровня": "Level Low",
        "Пуск АСПТ": "ASPT Start",
        "Сброс пуска АСПТ": "ASPT Start Reset",
        "Сброс тревоги": "Line Alarm Reset",
        "Снят с охраны": "Disarmed",
        "Срабатывание СДУ": "SDU",
        "Сработка извещателя": "Notifier",
        "Температура в норме": "Temperature Normal",
        "Тест извещателя": "Notifier Test",
        "Тихая тревога": "Silent Alarm",
        "Требует обслуживания": "Need Maintenance",
        "Тревога входа": "Alarm: Enter",
        "Тревога проникновения": "Intrusion Alert",
        "Уровень в норме": "Level Normal"
    }
}
```