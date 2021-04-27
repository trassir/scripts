# PTZ Automation

## **Основные функции**

Скрипт позволяет автоматизировать работу оператора с поворотной камерой.

При бездействии оператора, скрипт переведет камеру в один из следующих режимов:

- Переход по пресетам камеры
- Переход в пресет

## **Установка**

Скрипт необходимо добавить в разделе Автоматизация->Новый скрипт→Загрузить пример->Из файла.
После загрузки скрипта необходимо нажать на кнопку «Сохранить, запустить», снять галочку «Включить скрипт» и выполнить его настройку.

## **Настройка скрипта**

![img](https://confluence.trassir.com/download/attachments/6130336/image2020-5-28_12-27-55.png?version=1&modificationDate=1590658075000&api=v2)

1. Channel - выбор канала
2. Work by shedule - выбор расписания, если расписание не выбрано будет включен режим работы "Default mode"

![img](https://confluence.trassir.com/download/attachments/6130336/image2020-5-28_12-31-6.png?version=1&modificationDate=1590658266000&api=v2)

1. Default mode (Green or without schedule). Default mode: если расписание не выбрано, камера будет работать по заданному режиму. При выборе расписания - камера перейдет в заданный режим работы, когда расписание находится в зеленом цвете.
2. Alarm mode - расписание находится в красной зоне
3. Other mode - расписание находится в синей зоне

![img](https://confluence.trassir.com/download/attachments/6130336/image2020-5-28_12-43-23.png?version=1&modificationDate=1590659003000&api=v2)

1. Default preset - укажите пресет для работы в режиме Preset
2. Patrol path - путь патрулирования в режиме Patrol
3. Preset timeout, sec - время ожидания при переходи на следующий пресет в режиме Patrol
4. Max random preset timeout, sec. Если **Preset timeout** = **Max random preset timeout** время при переходе по пресетам будет одинаковым, для перехода по пресетам с рандомным временем **Max random preset timeout** должен быть больше **Preset timeout.**

> Для параметра **Preset timeout** и **Max random preset timeout** не рекомендуется выставлять значение <15, т.к это может повлиять на работу механической части камеры. 

**![img](https://confluence.trassir.com/download/attachments/6130336/image2020-5-28_13-9-48.png?version=1&modificationDate=1590660588000&api=v2)**

- ActiveDome timeout, sec - Если камера задействована в модуле ActiveDome, данный параметр определяет через какое время скрипт продолжит работу, в случае отсутствия команд от модуля ActiveDome.

![img](https://confluence.trassir.com/download/attachments/6130336/image2020-5-28_13-14-43.png?version=1&modificationDate=1590660882000&api=v2)

- Debug mode - режим отладки скрипта. Файл с логами скрипта сохраняется в папке скриншотов. 

