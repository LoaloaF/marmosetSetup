import requests
from time import sleep
import time

def test_endpoints():
    base_url = "http://localhost:8000"

    # GET /parameters
    # response = requests.get(f"{base_url}/parameters")
    # print("GET /parameters:", response.json())

    # # PATCH /parameters/{key}
    # key = "LOGGING_LEVEL"  # replace with your key
    # new_value = "DEBUG"  # replace with your value
    # response = requests.patch(f"{base_url}/parameters/{key}?new_value={new_value}")
    # print(f"PATCH /parameters/{key}:", response.json())

    def run():
        # POST /initiate
        response = requests.post(f"{base_url}/initiate")
        print("POST /initiate:", response.json())

        # POST /shm/create_termflag_shm
        response = requests.post(f"{base_url}/shm/create_termflag_shm")
        print("POST /shm/create_termflag_shm:", response.json())

        # POST /shm/create_ballvelocity_shm
        response = requests.post(f"{base_url}/shm/create_ballvelocity_shm")
        print("POST /shm/create_ballvelocity_shm:", response.json())

        # POST /procs/open_stream_portenta_proc
        response = requests.post(f"{base_url}/procs/launch_stream_portenta")
        print("POST /procs/open_stream_portenta_proc:", response.json())


        # POST /shm/create_portentaoutput_shm
        response = requests.post(f"{base_url}/shm/create_portentaoutput_shm")
        print("POST /shm/create_portentaoutput_shm:", response.json())

        # POST /shm/create_portentainput_shm
        response = requests.post(f"{base_url}/shm/create_portentainput_shm")
        print("POST /shm/create_portentainput_shm:", response.json())

        # POST /procs/open_por2shm2por_sim_proc
        response = requests.post(f"{base_url}/procs/launch_por2shm2por_sim")
        print("POST /procs/open_por2shm2por_sim_proc:", response.json())
        
        # POST /procs/open_por2shm2por_proc
        response = requests.post(f"{base_url}/procs/launch_por2shm2por")
        print("POST /procs/open_por2shm2por_proc:", response.json())
        
        # POST /procs/open_log_portenta_proc
        response = requests.post(f"{base_url}/procs/launch_log_portenta")
        print("POST /procs/open_log_portenta_proc:", response.json())
        
        # response = requests.post(f"{base_url}/raise_term_flag")

        # POST /procs/open_stream_portenta_proc
        response = requests.post(f"{base_url}/procs/launch_stream_portenta")
        print("POST /procs/open_stream_portenta_proc:", response.json())

    run()
    sleep(15)
    # POST /term_session
    response = requests.post(f"{base_url}/raise_term_flag")
    print("POST /raise_term_flag:", response.json())
    
    run()
    # POST /term_session
    response = requests.post(f"{base_url}/raise_term_flag")
    print("POST /raise_term_flag:", response.json())

    
if __name__ == "__main__":
    test_endpoints()