# -*- coding: utf-8 -*-
# Author:   zhouju
# At    :   2024/2/23
# Email :   zhouju@sunline.com
# About :   https://blog.codingcat.net
import logging

from celery import Celery, Task
from celery.signals import task_postrun, task_prerun


class MyTask(Task):
    def apply_async(self, args=None, kwargs=None, task_id=None, producer=None,
                    link=None, link_error=None, shadow=None, **options):
        # TODO 创建任务记录，任务信息name、func执行函数、id、createTime创建时间，status为created，进度0%，exception异常信息，result返回结果
        rst = super().apply_async(args=args, kwargs=kwargs, task_id=task_id, producer=producer,
                                  link=link, link_error=link_error, shadow=shadow, **options)
        # TODO 更新任务celery任务Id   会不会出现任务已发送给消费者，但是未更新任务对应celery的任务id，，，这样会导致后续无法更新状态或结果
        return rst


app = Celery('proj',
             broker='redis://127.0.0.1:6379',
             backend='rpc://',
             include=['proj.tasks'],
             task_cls=MyTask)

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule = {
    'add-every-30-seconds': {
        'task': 'proj.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

app.autodiscover_tasks()

app.conf.timezone = 'UTC'


@task_prerun.connect
def task_pre_run_callback(sender, task_id, task, *args, **kwargs):
    """
    # 回调的数据
    sender=<@task: mone.tasks.tasks.execute_task of tasks at 0x7f8a30c65da0>
    kwargs = {
     'signal': <Signal: task_prerun providing_args={'kwargs', 'args', 'task_id', 'task'}>,
     'task_id': 'a602189f-b0bb-4d83-8241-2a6d2c14a8ec',
     'task': <@task: mone.tasks.tasks.execute_task of tasks at 0x7f8a30c65da0>,
     'args': [],
     'kwargs': {'func_name': 'aps_radc.tasks.handlers.task_change_element',
                'func_data': {},
                'func_kwargs': {},
                'event_name': 'space/WEMXXT/change_element',
                 'expires_at': 0,
                'link_id': 'a602189f-b0bb-4d83-8241-2a6d2c14a8ec',
                'link_pre_func': 'aps_radc.tasks.callback.on_task_pre_callback',
                'link_post_func': 'aps_radc.tasks.callback.on_task_post_callback'
                }
    }

    :param sender:
    :param task_id:
    :param task:
    :param kwargs:
    :return:
    """
    print(task_id)
    logging.error('vvvvvvvv')
    print('prerun')


@task_postrun.connect
def task_post_run_callback(sender, task_id, task, retval, **kwargs):
    """ 任务执行完成的回调
    # 回调的数据
    sender  = < @task: mone.tasks.tasks.execute_task of tasks at 0x7fb621f91cc0 >
    task_id = 'a602189f-b0bb-4d83-8241-2a6d2c14a8ec',
    task    =  <@task: mone.tasks.tasks.execute_task of tasks at 0x7f8a30c65da0>,
    retval  = {
                'rc': True,
                'status': 'SUCCESS',
                'message': '',
                'startTime': '2023-12-29 13:13:19',
                'endTime': '2023-12-29 13:13:22',
                'task': {
                    'func_name': 'aps_radc.tasks.handlers.task_change_element',
                    'CELERY_TASK_HOSTNAME': 'celery@rbtnode1',
                    'CELERY_TASK_ID': '26a3342b-b270-492f-afdc-5669f02abb2c'
                },
                'result': {
                    'rc': True,
                    'message': '',
                    'data': {
                        'todo_list_id': '658e557298391f40e6972167',
                        '..': ''
                    },
                    'returnData': {}
                }
            }

    :param sender:
    :param task:
    :param task_id:
    :param retval: 这个是返回的结果值
    :param kwargs:
    :return:
    """
    print('postrun')


if __name__ == '__main__':
    app.start()
