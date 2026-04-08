PLAY [Install Clickhouse] **********************************************************************************************

TASK [Gathering Facts] *************************************************************************************************
ok: [clickhouse-01]

TASK [Install clickhouse packages directly from URLs] ******************************************************************
ok: [clickhouse-01]

TASK [Ensure clickhouse-server is running] *****************************************************************************
ok: [clickhouse-01]

TASK [Create database if not exists] ***********************************************************************************
changed: [clickhouse-01]

PLAY [Install and configure Vector] ************************************************************************************

TASK [Create vector user] **********************************************************************************************
ok: [clickhouse-01]

TASK [Create vector directories] ***************************************************************************************
ok: [clickhouse-01] => (item=/opt/vector)
ok: [clickhouse-01] => (item=/etc/vector)

TASK [Download Vector archive] *****************************************************************************************
ok: [clickhouse-01]

TASK [Extract Vector archive] ******************************************************************************************
ok: [clickhouse-01]

TASK [Create symlink to vector binary] *********************************************************************************
ok: [clickhouse-01]

TASK [Deploy Vector configuration] *************************************************************************************
changed: [clickhouse-01]

TASK [Create Vector systemd service] ***********************************************************************************
ok: [clickhouse-01]

TASK [Start and enable Vector service] *********************************************************************************
ok: [clickhouse-01]

RUNNING HANDLER [Restart vector service] *******************************************************************************
changed: [clickhouse-01]

PLAY RECAP *************************************************************************************************************
clickhouse-01              : ok=13   changed=3    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
