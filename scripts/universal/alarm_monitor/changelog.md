### 2021.04.06 Version 2.12.5
- В разделе "Опциональные настройки ТМ" добавлен пункт "Зафиксировать ячейку для каждого канала при отображении". Если отмечен данный чекбокс, то тревожный канал каждый раз отображается в одной и той же ячейке на тревожном мониторе.


### 2021.03.23 Version 2.12.4
- Рефакторинг. Работа с объектами Trassir без фреймворка TSF.

### 2021.03.03 Version 2.12.3
-Добавлена работа по событиям скрипта детектора подозрительных поз.

### 2021.02.16 Version 2.12.2
- Добавлена работа с событиями от канала: сигнал потерян, сигнал восстановлен.

### 2021.02.11 Version 2.12.1
- Добавлена реакция по скорости движения объекта (от детектора SIMT)

### 2021.02.02 Version 2.12.0
- в операции со СКУД добавлена возможность работы со СКУД Hikvision

### 2020.12.30 Version 2.11.9
- добавлена возможность использования прокси в локальной сети для TbotAPI
- исправлен баг в модуле по работе с Orion, который приводит к ошибке скрипта если не задан ассоциированный канал. 

### 2020.12.30 Version 2.11.8
- Исправлена ошибка  `TypeError: send() got unexpected keyword argument channel` при 
отправки скриншота на почту


### 2020.12.11 Version 2.11.6
- добавлена возможность прикреплять видео при генерации тревог (инцидентов в Trassir Cloud) 


### 2020.12.09 Version 2.11.5
- исправлен баг отображения на тревожном шаблоне если окно
 программы находится в свернутом состоянии: если
 окно программы сворачивается при просмотре любого не тревожного 
 шаблона, то при наступлении тревожного события, тревожные каналы
 добавляются на этот шаблон.

### 2020.11.14 Version 2.11.4 
- Добавлен перевод на китайский 
- Поправлены баги с локализацией


### 2020.11.13 Version 2.11.3
- Переписан модуль детекции длительного присутствия в зоне (нейродетекции),
теперь скрипт может запускаться на серверах с модулем numpy до 1.12
-Поправлены недочеты перевода

### 2020.11.13 Version 2.11.2
- fix bug при удалении старых скриншотов

### 2020.10.29 Version 2.10.2
- Добавлена настройка: Имя папки для сохранения скриншотов

Если `default` или `""` имя папки `AlarmMonitor_` + `guid script`

### 2020.10.13 Version 2.10.1
- Исправлена ошибка `ValueError: unsupported format character...`

### 2020.10.06 Version 2.10.0
- Добавлена возможность установить задержку запуска скрипта после старта трассира

### 2020.09.09 Version 2.9.3
- Поправлен код для реагирования от кастомных событий

### 2020.08.26 Version 2.9.2
- Добавлена возможность выбора типа событий от системы ВОРОН для реакции

### 2020.08.18 Version 2.9.1
- Добавлена задержка перед сохранением скриншота
- Обновлен модуль shot_saver


### 2020.08.10 Version 2.9.0 
- Добавлена реакция на события с каналов ассоциированных с охранной системой ВОРОН
  (В Trassir должен быть запущен скрипт интеграции с системой ВОРОН)
- Добавлена возможность выбора типа события для системы СКУД GATE
- Добавлена возможность генерации тревог

### 2020.08.10 Version 2.8.2 
- Добавлена реакция на события с каналов ассоциированных с охранной системой ВОРОН
  (В Trassir должен быть запущен скрипт интеграции с системой ВОРОН)


### 2020.08.05 Version 2.8.1
- Спец символы в нaзвании канала заменяются знаком _  (подчёркивание) при формировании имени файла скриншота

### 2020.08.04 Version 2.8.0
- Добавлена работа по нейродетекциям, когда объект длительное время присутствует в заданной зоне
- В тексте уведомлений убраны теги для отправки сообщений в Telegram. Наличие тегов приводило к ошибке отправки сообщений.
- Починена отправка на почту текстовых уведомлений

### 2020.07.30 Version 2.7.5
-Обновлён модуль FTP, добавлена возможность выбора работы режима FTP: пассивный/ активный
-Telegram: host.exec_encoded(tbot_service) - вызывается в основном модуле.

#### 2020.07.21 Version 2.7.4
-Обновлен перевод для английского и турецкого языков.

#### 2020.07.17 Version 2.7.3
-Исправлена ошибка при работе с Orion в случае если ассоциированный канал не был указан, исправлена работа отображения тревожного канала.

#### 2020.07.07 Version 2.7.2
Исправлена ошибка работы по пересечению границ на канале с нейродетектором.

#### 2020.07.07 Version 2.7.1
- Добавлена возможность указать абсолютный путь к .wav файлу для воспроизведения звукового оповещения

#### 2020.07.09 Version 2.63
- Убрана проверка выбранных границ для работы, т.к. иногда скрипт загружается раньше,
чем объекты выбранных границы. Из-за чего может появляться ошибка.

#### 2020.06.30 Version 2.62
- исправлена работа отображения тревожного канала при включенном чекбоксе "Сброс тревоги только при отсутствии движения на канале"

#### 2020.06.25
- При работе по событиям deep detections 
  исправлено получение имя зоны с zone_name = getattr(zone, "zone_name", getattr(zone, "name"))
  на zone_name = getattr(zone, "zone_name", getattr(zone, "name", None))

#### 2020.06.22 Version 2.6
- Добавлен параметр 'Не более одного скриншота за период'. Параметр нужен для того, чтобы 
ограничить количество скриншотов за заданный промежуток времени с одного канала, когда в единицу 
времени происходит большое количество событий на канале.
- Добавлена работа с Aruco кодами

#### 2020.06.18 Version 2.5
- Добавлена возможность сохранять скриншот в субпотоке

#### 2020.06.02 Version 2.4
- Добавлена работа People Detected от HW детектора камеры Hikvision
- В модуле delete_old_shots удаление осуществляется с помощью shutil.rmtree, до этого использовалось os.removedirs()

#### 2020.05.28 Version 2.34
- Обновлен перевод на китайский

#### 2020.05.26 Version 2.33

- Исправлена чрезмерная нагрузка на сервер при работе скрипта со скриншотами: [SCR-5196](https://support.trassir.com/browse/SCR-5196)


#### 2020.05.20 Version 2.32

- Добавлено реагирование скрипта на события от [AutoUniversal](https://confluence.trassir.com/display/WD/Auto+Universal) с версии 2.2


#### 2020.05.13 Version 2.31

- Изменена работа по расписанию. Если в разделе "Дополнительно" выбрано расписание, то скрипт отрабатывает, когда расписание находится в красной зоне. 
- Исправлен баг при задании работы по расписанию:  [SCR-5236](https://support.trassir.com/browse/SCR-5236)