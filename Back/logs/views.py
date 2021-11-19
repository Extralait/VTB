from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.template import loader

from logs.models import Entry
from utils import db


@staff_member_required
def logs(request):
    entries = []
    log_events = {

    }
    for log_event, event_title in log_events.items():
        entries.append(list(reversed(db.query(Entry, kind=log_event))))
    headers = [t for t in log_events.values()]
    rows = []

    i = 0
    while True:
        row = []
        for entry_pack in entries:
            if len(entry_pack) >= (i + 1):
                row.append(entry_pack[i])
            else:
                row.append(None)
        print(i, row)
        if i > 500 or not any(row):
            break
        i += 1
        rows.append(row)

    template = loader.get_template('logs.html')
    rendered = template.render({'headers': headers, 'rows': rows}, request)
    return HttpResponse(rendered)
