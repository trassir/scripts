## Основные функции
Скрипт запоминает последнее событие от AutoTrassir и отправляет полученные данные POST запросом на указанный в настройках скрипта url адрес.

## Установка
* Перейти в автоматизацию, нажать «Загрузить пример» и выбрать «Из файла», указав путь к скрипту.
* Снять галочку «Включить скрипт» и нажать сохранить.
* Выполнить настройку и нажать "Сохранить и запустить".

## Настройка
<img src="settings.png" alt="settings.png" align=left>

**URL -** полный URL адрес для POST запроса

**Debug -** режим отладки, если данный чекбокс активирован, то в папку скриншотов будет сохраняться лог скрипта.

### Пример данных которые отправляются POST запросом
```python
{
  "id": 931416,
  "plate": "a777aa7?",
  "best_guess": "a777aa77",
  "radar_speed": 0.0,
  "country": "ru",
  "lane": 1,
  "server": {
    "name": "SERVER_NAME",
    "guid": "SERVER_GUID"
  },
  "channel": {
    "name": "CHANNEL_NAME",
    "guid": "CHANNEL_GUID"
  },
  "direction": "DOWN",
  "vehicle_type": "car",
  "quality": 80.14884185791016,
  "time_enter": 1601291186685565,
  "time_bestview": 1601291190660987,
  "time_leave": 1601291191734351,
  "matched_embrecords_history": [
    {"reaction": 1, "comment": ""},
    {"reaction": 2, "comment": "embrecord"}
  ],
  "matched_extlists_history": [
    {"reaction": 1, "comment": "extrecord"}
  ],
}
```

**id: number** - уникальный идентификатор события.

**plate: string** - распознанный номер, возможно со знаками "?" на месте неуверенных символов.

**best_guess: string** - распознанный номер, без "?".

**radar_speed: number** - скорость ТС (если используется интеграция с радаром).

**country: string** - страна шаблона если распознана, возможна пустая строка.

**lane: number** - номер линии, по которой проехала машина.

**server: object** - информация о сервере с которого пришло событие.

- **name: string** - имя сервера, с которого пришло событие.
- **guid: string** - guid сервера, с которого пришло событие.

**channel: object** - информация о канале с которого пришло событие.

- **name: string** - имя канала, с которого пришло событие.
- **guid: string** - guid канала, с которого пришло событие.

**direction: string**- направление движения.

**vehicle_type: string** - тип машины. Используется только в LPR5, возможные варианты:

- car - легковой автомобиль
- motorcycle - мотоцикл
- bus - автобус
- truck - грузовик
- van - автофургон

**quality: number** - уверенность детекции в time_bestview от 0 до 100.

**time_enter: number** - timestamp въезда авто в кадр.

**time_bestview: number** - timestamp наилучшего кадра для распознавания номера.

**time_leave: number** - timestamp выезда авто из кадра.

**matched_embrecords_history: array of objects** - где был найден номер(внутренние списки).

- **reaction: number** - реакция. Возможные варианты: 0 - чёрный список, 1 - информационный список, 2 - белый список.
- **comment: string** - комментарий, возможно пустой.

**matched_extlists_history: array of objects** - где был найден номер(внешние списки).

- **reaction: number** - реакция. Возможные варианты: 0 - чёрный список, 1 - информационный список, 2 - белый список.
- **comment: string** - комментарий, возможно пустой.