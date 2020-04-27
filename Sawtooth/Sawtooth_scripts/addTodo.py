import requests
requests.post("http://localhost:8888/todo", 
                  json={"Title":"my first todo", 
                        "Description":"my first todo"})