from flask_cors import CORS
from flask import Flask, jsonify,request
from generators.process import process_event_generator
from generators.SQL_server_security import sql_event_generator 
from generators.windows_event import generate_windows_events
from generators.suricata_events import generate_suricata_events
from generators.active_directory import directory_events_loop
from generators.sflow import generate_sFlow
from storageHandler import store_event_in_file

app = Flask(__name__)
CORS(app)

defaultFiles = {
    "system-process" : "sytem_events.txt",
    "sql-server" : "sql_server.txt",
    "windows_gen":"windows_events.txt",
    "suricata_event" : "suricata_events.txt",
    "directory_events": "directory_events.txt",
    "sFlow_events" : "sFlow_events.txt"
}

@app.route('/system-process', methods=['GET'])
def generate_events():
    events = []
    eventQty = int(request.args.get('qty'))
    saveLog = bool(int(request.args.get('savelog')))
    for _ in range(eventQty):
        event = process_event_generator() 
        events.append(event)
    if saveLog:
        file_name = request.args.get('filename')
        if not file_name:
            file_name = defaultFiles['system-process']
        store_event_in_file(file_name = file_name, event_data = events)
    return jsonify(events)

@app.route('/sql-server-events',methods=['GET'])
def generate_sql_events():
    eventQty = int(request.args.get('qty'))
    saveLog = bool(int(request.args.get('savelog')))
    events = [sql_event_generator() for _ in range(eventQty)]
    if saveLog:
        file_name = request.args.get('filename')
        if not file_name:
            file_name = defaultFiles['sql-server']
        store_event_in_file(file_name=file_name,event_data=events)
    return jsonify(events)

@app.route('/windows-generator-event',methods=['GET'])
def windows_event():
    eventQty = int(request.args.get('qty'))
    saveLog = bool(int(request.args.get('savelog')))
    events = generate_windows_events(eventQty)
    if saveLog:
        file_name = request.args.get('filename')
        if not file_name:
           file_name = defaultFiles['windows_gen']
        store_event_in_file(file_name = file_name,event_data = events)
    return jsonify(events)

@app.route('/suricata-events',methods=['GET'])
def suricata_events():
    eventQty = int(request.args.get('qty'))
    saveLog = bool(int(request.args.get('savelog')))
    events = generate_suricata_events(eventQty)
    if saveLog:
        file_name = request.args.get('filename')
        if not file_name:
            file_name = defaultFiles['suricata_event']
        store_event_in_file(file_name = file_name,event_data = events)
    return jsonify(events)

@app.route('/directory-events',methods=['GET'])
def generate_directory_events():
    eventQty = int(request.args.get('qty'))
    saveLog = bool(int(request.args.get('savelog')))
    events = directory_events_loop(eventQty)
    if saveLog:
        file_name = request.args.get('filename')
        if not file_name:
            file_name = defaultFiles['directory_events']
        store_event_in_file(file_name = file_name,event_data = events)
    return jsonify(events)

@app.route('/sFlow-events',methods = ['GET'])
def sFlow():
    eventQty = int(request.args.get('qty'))
    saveLog = bool(int(request.args.get('savelog')))
    events = directory_events_loop(eventQty)
    if saveLog:
        file_name = request.args.get('filename')
        if not file_name:
            file_name = defaultFiles['sFlow_events']
        store_event_in_file(file_name = file_name,event_data = events)
    return jsonify(events)



if __name__ == "__main__":
    app.run(debug=True)