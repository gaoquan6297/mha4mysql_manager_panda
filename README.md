# 描述
```
1. proxysql根据后端mysql节点的read_only状态来判断主从角色
2. mha实现主从自动切换以及调用master_ip_failover脚本实现额外的附加动作，本例主要实现当主从发生切换时，将old_master节点从proxysql摘除
3. 由于proxysql启动用cluster同步，所以只需要从其中一个proxysql节点删除old_master节点即可
```
# 部署架构
```
proxysql node and mysql node deploy on the same node.
proxysql should with cluster mode.
```
# 
