import requests, json

def completed_tasks():
    result = requests.get(
        'http://127.0.0.1:5001/completed',
        headers={'content-type': 'application/json'},
    )
    print(f'Your request for completed tasks was successful: {result}')
    return result.json()
if __name__ == '__main__':
    print (completed_tasks())
    
def add_tasks(TaskTitle, TaskDescription, Completed):
        new_task = {
            'TaskTitle': TaskTitle,
            'TaskDescription': TaskDescription,
            '1': Completed
        }
                
        result = requests.get(
            'http://127.0.0.1:5001/add',
            headers={'content-type': 'application/json'},
            data=json.dumps(new_task)
    )

        return result.json()
    
if __name__ == '__main__':
    add_tasks('testtitle', 'testdescr'', '1')
    
