## preparation

running deepseek r1 on a mac m1,2,3 machine

you will need ollama (software to run deepseek/llms locally) and chatbox (GUI)

on mac:

```bash
brew install ollama
brew install --cask chatbox
```

## usage

select the right vram size

https://ollama.com/library/deepseek-r1:14b

e.g.

- 16 GB (V)RAM -> 14b
- 8 GB (V)RAM -> 8b
- 64 GB (V)RAM -> 32b

```bash
ollama run deepseek-r1:14b
```
