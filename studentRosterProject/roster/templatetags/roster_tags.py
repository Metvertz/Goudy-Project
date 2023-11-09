from django import template
register = template.Library()

@register.simple_tag
def get_schedule(schedule_matrix, worker, day):
    return schedule_matrix.get(worker, {}).get(day, '')