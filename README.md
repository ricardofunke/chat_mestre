Dependências:

- python 3.11
- virtualenv

```
git clone git@github.com:ricardofunke/chat_mestre.git
cd chat_mestre/prototipo_python
virtualenv venv
source venv/bin/activate
pip install environs openai
export PYTHONPATH=`pwd`
cd common
python openai_calls.py
```
