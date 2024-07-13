from flask import Flask, Response
import time
import os, json
app = Flask(__name__)

def frames(dir):
    with open(f'{dir}/config.json')as f:
        config = json.load(f)
    frames = []
    for i in range(len(os.listdir(dir))-1):
        with open(f'{dir}/{i+1}.txt', encoding='utf-8')as f:
            frame = f.read()
            if str(i+1) in list(config.keys()):
                for key, value in config[str(i+1)].items():
                    frame.replace(key, f'\033[38;2;{value[0]};{value[1]};{value[2]}m{key}\033[0m')
                    frames.append(frame)
            else:
                frames.append(frame)
    return frames


clear_screen = "\033[2J\033[H"

@app.route('/hello-kitty-hearts-1')
def animation():
    def generate():
        while True:
            for frame in frames('hello-kitty-hearts-1'):
                yield clear_screen + frame + '\n'
                time.sleep(0.3)

    return Response(generate(), content_type='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
    #frames('hello-kitty-kiss')
