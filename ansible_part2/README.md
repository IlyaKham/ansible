# Ansible Playbook для установки ClickHouse, Vector и LightHouse на CentOS 7

## 📖 Описание

Данный playbook автоматизирует установку и настройку трёх сервисов на отдельных серверах CentOS 7 с использованием **Ansible Roles**:

- **ClickHouse** (v22.3.3.44) - колоночная СУБД для аналитики и хранения логов
- **Vector** (v0.21.1) - инструмент для сбора, трансформации и маршрутизации логов
- **LightHouse** - легковесный веб-интерфейс для ClickHouse

Playbook использует отдельные репозитории с ролями:
- [clickhouse-role](https://github.com/IlyaKham/clickhouse-role)
- [vector-role](https://github.com/IlyaKham/vector-role)
- [lighthouse-role](https://github.com/IlyaKham/lighthouse-role)

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
# Создайте виртуальное окружение
python3 -m venv ansible-env

# Активируйте окружение
source ansible-env/bin/activate

# Установите совместимую версию Ansible
pip install 'ansible==4.10.0'

# Проверьте версию
ansible --version
# Должно быть: ansible [core 2.11.x]


### Структура проекта:

ansible/
├── inventory/
│   └── prod.yml                 # Inventory файл с хостами
├── group_vars/
│   ├── clickhouse/
│   │   └── vars.yml             # Переменные ClickHouse
│   ├── vector/
│   │   └── vars.yml             # Переменные Vector
│   └── lighthouse/
│       └── vars.yml             # Переменные LightHouse
├── requirements.yml             # Зависимости (ссылки на роли)
├── site.yml                     # Основной playbook
├── ansible.cfg                  # Конфигурация Ansible
├── .gitignore                   # Игнорируемые файлы
└── README.md                    # Документация

### Установка ролей:

ansible-galaxy install -r requirements.yml -p roles/