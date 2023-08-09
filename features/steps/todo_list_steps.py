from behave import given, when, then
import sys
sys.path.append('/home/networking/Proyects/SW2/TODO')
from todo_list import TodoListManager
# from ... import todo_list
# from ...todo_list import TodoListManager

@given('the to-do list is empty')
def step_impl(context):
# Set the to-do list as an empty list
    global to_do_list
    to_do_list = []

 
@when('the user adds a task "{task}"')
def step_add_task(context, task):
    context.todo_list.add_task(task)

@then('the to-do list should contain "{task}"')
def step_check_task(context, task):
    assert any(item['name'] == task for item in context.todo_list.tasks)

@when('the user lists all tasks')
def step_list_all_tasks(context):
    context.list_output = []
    def capture_output(output):
        context.list_output.append(output)
    context.todo_list.list_tasks = capture_output

@then('the output should contain:')
def step_check_output(context):
    expected_output = context.text.split('\n')
    assert all(item in context.list_output for item in expected_output)

@when('the user marks task "{task}" as completed')
def step_mark_task_completed(context, task):
    context.marked_task = context.todo_list.mark_task_completed(task)

@then('the to-do list should show task "{task}" as completed')
def step_check_task_status(context, task):
    assert context.marked_task and any(item['name'] == task and item['status'] == 'Completed' for item in context.todo_list.tasks)

