# importa o jquery
q = require('jquery')

# importa outras libs
require('bootstrap')
bootbox = require('bootbox')

class TaskManager(object):
    def __init__(self):
        self.tasks = []
        self.q_task = q('#task')
        self.q_tasks = q('#task-list')
        self.add_listeners()

    def add_task(self, task):
        if len(self.tasks) == 0:
            self.q_tasks.html('')
        self.tasks.append(task)
        self.q_tasks.append(f'<li class="list-group-item">{task} <button class="btn btn-danger btn-xs">&times;</button></li>')

    def remove_task(self, q_item):
        index = q_item.index()
        q_item.remove()
        self.tasks.pop(index)
        if len(self.tasks) == 0:
            self.q_tasks.html('<li class=list-group-item>No task registered</li>')

    def on_add_task(self):
        def _on_add_task(event):
            if event.which == 13 and q.trim(event.target.value) != '':
                self.add_task(event.target.value)
                event.target.value = ''

        return _on_add_task

    def on_remove_task(self):
        def _on_remove_task(event):
            def confirm_callback(result):
                if result:
                    q_item = q(event.currentTarget).parents('li')
                    self.remove_task(q_item)
            bootbox.confirm('Are you sure?', confirm_callback)

        return _on_remove_task

    def add_listeners(self):
        self.q_task.on('keyup', self.on_add_task())
        self.q_tasks.on('click', '.btn-danger', self.on_remove_task())


module.exports = TaskManager
