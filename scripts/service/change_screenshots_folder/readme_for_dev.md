# Screenshot Folder Changer

Скрипт изменяет папку скриншотов. Если при установке новой папки
возникли ошибки - скрипт сделает еще две попытки изменить папку.
Кол-во попыток можно изменить указав необходимое значение функции
`FolderSetter.set_folder(tries=3)`

Чаще всего ошибки могут возникнуть при монтировании сетевой папки 
(при вводе неверных данных для подключения) или папки на HDD (при
отсутствии в системе диска)

Возможные значение:

- Default
- HDD
- Network (CIFS)
- Custom

## Default

Устанавливает путь по умолчанию `"/home/trassir/shots"`

## HDD

Устанавливает путь к папке скриншотов на HDD:
`/media/TrassirArchive*/TrassirArbitraryData/shots`

При наличии нескольких HDD в системе пути 
`/media/TrassirArchive*` монтируются динамически и при каждой 
загрузке меняются. Поэтому скрипт создает папку `shots` в каталоге, 
возвращаемом методом `host.path_arbitrary_data`. 

По этой-же причине **при выборе данного пункта нельзя 
отключать или удалять скрипт**.

Если в системе нет ни одного HDD метод `host.path_arbitrary_data` 
вернет пустую строку, а скрипт выпадет в ошибку 
`EnvironmentError("HDD Not Found!...")`

## Network (CIFS)

Монтирует общую сетевую папку в локальную `/mnt/LocalStorage/shared`
после чего устанавливает ее в качестве папки скриншотов.

Монтирование папки реализуется по протоколу CIFS. 
При этом чтобы расшарить папку на **Windows 10 ** необходимо 
предварительно включить компонент Windows: **SMB 1.0/CIFS File
Sharing Support** (*название компонента может отличаться 
в зависимости от версии Windows*). На более ранних версиях Windows
данный компонент может отсутствовать, соотвественно поддержка 
данного протокола включена по умолчанию.

При расшаривании папки обязательно укажите пользователя и пароль.
Анонимный доступ может не сработать, даже если в настройках доступа
к расшареной папке разрешено чтение/изменение всем.

### WARNING

При потере соеднения с папкой все обращения к папке скриншотов 
могут "подвесить" trassir на 120 сек. 

## Custom

Устанавливает папку, которую пользователь укажет. По умолчанию
содает папку, если она не существует

# For developers

Вы можете добавить новый тип папки, например примонтировать ftp
папку и установить ее в качестве папки скриншотов. 

Создайте свой класс наследуя абстрактный класс `ShotsFolder`,
у которого необходимо переопределить основной метод `mount`.

```python
import os


class TempFolder(ShotsFolder):
    _FOLDER = "/tmp/shots"
    def mount(self):
        if not os.path.isdir(self._FOLDER):
            os.mkdirs(self._FOLDER)
        
        return self._FOLDER
```

Можно настроить действия, которые будут выполнятсья 
при отключении скрипта. Например "размонтирование" папки,
или удаление временных файлов.

```python
import os
import shutil


class TempFolder(ShotsFolder):
    _FOLDER = "/tmp/shots"
    def mount(self):
        if not os.path.isdir(self._FOLDER):
            os.mkdirs(self._FOLDER)
        
        return self._FOLDER
        
    def umount(self):
        shutil.rmtree(self._FOLDER)
        return self._DEFAULT
        
```

По желанию можно установить аттрибут `rollback = True` тогда 
при отключении скрипта в качестве папки скриншотов будет установленно
значение, которое возвращает метод `ShotsFolder.umount`

```python
import os
import shutil


class TempFolder(ShotsFolder):
    _FOLDER = "/tmp/shots"
    
    def __init__(self):
        self.rollback = True
    
    def mount(self):
        if not os.path.isdir(self._FOLDER):
            os.mkdirs(self._FOLDER)
        
        return self._FOLDER
        
    def umount(self):
        shutil.rmtree(self._FOLDER)
        return self._DEFAULT
        
```
