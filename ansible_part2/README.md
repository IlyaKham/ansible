# Ansible Playbook для установки ClickHouse, Vector и LightHouse на CentOS 7

## 📖 Описание

Данный playbook автоматизирует установку и настройку трёх сервисов на отдельных серверах CentOS 7:

- **ClickHouse** (v22.3.3.44) - колоночная СУБД для аналитики и хранения логов
- **Vector** (v0.21.1) - инструмент для сбора, трансформации и маршрутизации логов
- **LightHouse** - легковесный веб-интерфейс для ClickHouse

Playbook учитывает все особенности CentOS 7:
- Использование Python 2 для ClickHouse (совместимость с yum)
- Использование Python 3 для Vector и LightHouse
- Настройка SELinux для Nginx
- Установка EPEL репозитория для nginx
- Настройка ClickHouse для приёма внешних подключений

## ⚙️ Требования к управляющей машине

### Версии Ansible

**Важно:** Для работы с CentOS 7 требуется использовать **Ansible 4.10.0** (ansible-core 2.11.x), так как более новые версии требуют Python 3.8+ на целевых хостах.

| Компонент | Требуемая версия | Причина |
|-----------|-----------------|---------|
| **Ansible** | 4.10.0 | Совместимость с Python 3.6 на CentOS 7 |
| **ansible-core** | 2.11.x | Поддержка старых версий Python |
| **Python** | 3.6+ | На управляющей машине |

### Создание виртуального окружения

Рекомендуется использовать виртуальное окружение для изоляции зависимостей:

```bash
# Установите Python 3.6+ на управляющей машине
# Создайте виртуальное окружение
python3 -m venv ansible-env

# Активируйте окружение
source ansible-env/bin/activate

# Установите совместимую версию Ansible
pip install 'ansible==4.10.0'

# Проверьте версию
ansible --version
# Должно быть: ansible [core 2.11.x]

Альтернативная установка без venv
bash
# Установка глобально (не рекомендуется)
pip install 'ansible==4.10.0'

# Или через пакетный менеджер (если доступен)
sudo yum install ansible-4.10.0

Cтруктура
ansible_part2/
├── inventory/
│   └── prod.yml                 # Inventory файл с хостами
├── group_vars/
│   ├── clickhouse/
│   │   └── vars.yml             # Переменные ClickHouse
│   ├── vector/
│   │   └── vars.yml             # Переменные Vector
│   └── lighthouse/
│       └── vars.yml             # Переменные LightHouse
├── templates/
│   ├── vector.toml.j2           # Шаблон конфига Vector
│   ├── vector.service.j2        # Шаблон systemd сервиса Vector
│   └── nginx_lighthouse.conf.j2 # Шаблон конфига Nginx
├── site.yml                     # Основной playbook
├── ansible.cfg                  # Конфигурация Ansible
├── .gitignore                   # Игнорируемые файлы
└── README.md                    # Документация

Playbook поддерживает теги для выборочного запуска:

Тег	Описание
clickhouse	Установка и настройка только ClickHouse
vector	Установка и настройка только Vector
lighthouse	Установка и настройка только LightHouse
Примеры использования тегов:
bash
# Установка только ClickHouse
ansible-playbook -i inventory/prod.yml site.yml --tags clickhouse --diff

# Установка только Vector
ansible-playbook -i inventory/prod.yml site.yml --tags vector --diff

# Установка только LightHouse
ansible-playbook -i inventory/prod.yml site.yml --tags lighthouse --diff

# Установка всех сервисов
ansible-playbook -i inventory/prod.yml site.yml --dif
