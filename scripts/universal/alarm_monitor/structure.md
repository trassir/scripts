## 
Структура проекта:
resources
|
|- reactions (folder) 
|	|     
|   | . . .
|   |
|   |-reactions (class Reactions. Все реакции добавляются 
|   |            и вызываются через этот класс)
|   |-executors 
|   |	|- executor (class Executor, __metaclass__ = abc.ABCMeta)
|   |	|- alarm_mon (class AlarmMonitorManager)
|   |	|- access_control (class AccessControlOperations)
|	|	|- play_sound (class PlaySound)
|	|	|- output_reactions (class OutputReactions)
|	|	|- output_reaction_v2 (class OutputReactionsII)
|	|	|- show_message (class ShowMessage)
|	|	|- show_popup (class ShowPopup)
|	|   |- reactions_with_screenshots (особый класс ReactionsWithScreenshots)
|	|   |- sms_sender (class SMSSendText)
|   |   |- telegram_text_sender (class TelegramSendText)
|   |
|   |
|	|- screenshots_senders_adopters (class AdoptedSender,
|	                     			 class Email,
|	     			    			 class FTP,
|	                    			 class Telegram
|	                  				 )
|
|
|- event_handlers
|    | 
|    |- dbase
|    |- simple_events
|    |- simt
|    |- face_recognizer
|    |- gpio_events
|    |- deep_detections
|    |- orion
|    |- sigur
|    
|      
|- helpers.py    
|- shot_saver
|- email_sender
|- schedule
|- constants
|- base_utils
|- ts_files

alarm_monitor_2.0


## Реакции скрипта
Один класс реакции отвечает за одну реакцию, например проигрывать звуковой файл.
Каждая реакция является потомком Executor с обязательным методом
Executor.execute(channel, tmstmp, alarm_messages, shot_name, *args, **kwargs)
Такой подход унифицирует систему и позволяет без труда добавлять новые реакции.

Объект класса Reactions представляет из себя интерфейс для добавления и вызова реакций. 
Для вызова реакций используется 

reactions.make_reactions(channel, tmstmp, alarm_messages, shot_name, *args, **kwargs)

Добавление определённой реакции скрипта на события выглядит таким образом:
```
reactions = Reactions(schedule_name="", schedule_color=None)
reactions.add_executor(executor)
```
где executor это объект, с родительским классом Executor.

Образец класса потомка (Executor) для проигрывания звука:

```
class PlaySound(Executor):
    def __init__(self, sound_name):
        self._path_to_sound_file = ''
        self.path_to_sound_file = sound_name
        # ...
    # ...
    
    def play_sound(self):
        logger.debug("Start play sound")
        if os.name == "nt":
            winsound.PlaySound(
                self.path_to_sound_file,
                winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOWAIT,
            )
        else:
            os.system(
                'aplay -D "{sound_device}" "{filename}" &'.format(
                    sound_device=self.default_sound_play_device,
                    filename=self.path_to_sound_file
                )
            )

    def execute(self, *args, **kwargs):
        self.play_sound()
```


### Реакций с использованием скриншота, ReactionsWithScreenshots

Расслыка скриншотов по сути представляет цепочку из двух действий: сделать сам скриншот и отправить его через email, Telegram, ftp и.т.д.

Для работы со скриншотами используется класс ReactionsWithScreenshots, этот класс являет потомком Executor

Через данный класс выполняется работа по созданию и отправлению скриншотов посредством различных объектов Senders.

Отличительная особенность ReactionsWithScreenshots:  класс обладает методом add_sender, через который добавляются классы различных AdoptedSender (mail, Telegram, ftp):

```self.senders[sender.__class__.__name__] = sender
```

При наступлении события в методе ReactionsWithScreenshots.execute
запускается задача на создание скриншота:

```
task_guid, file_path = self.shot_saver_obj.save(
        channel, dt, self.figures, callback=self.send_shots
    )
```

Когда, скриншот создатся запускатеся ReactionsWithScreenshots.send_shots, который
рассылает скриншот:

```
for s_name, sender in self.senders.iteritems():
    sender.send(state, file_path, alarm_messages)
```


## AdoptedSender
class AdoptedSender - абстрактный базовый класс. 
Задача создавать адаптеры к различным сендерам для отправки скриншотов.

```
class AdoptedSender(py_object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def send(self, success, shot_path, alarm_messages):       
        pass
```

Реализация класса для telegram_sender:

```
class AdoptedTelegramSender(AdoptedSender):
    def __init__(self, telegram_sender, ):
        self.telegram_sender = telegram_sender

    def send(self, success, shot_path, *args, **kwargs):
        if success:
            logger.debug("start try to send images to telegram")
            try:
                self.telegram_sender.image(shot_path)
            except Exception as err:
                logger.exception(err)
        else:
            logger.debug("Telegram sender. Nothing to send")