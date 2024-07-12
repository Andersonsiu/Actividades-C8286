# run_system.py
from actors.py import SupervisorActor
from event_stream import EventStreamActor

def main():
    supervisor = SupervisorActor.start()
    event_stream = EventStreamActor.start(supervisor)
    
    # Mantener el sistema en ejecución
    try:
        supervisor.proxy().get()
    except KeyboardInterrupt:
        print("Sistema detenido por el usuario.")

if __name__ == "__main__":
    main()
