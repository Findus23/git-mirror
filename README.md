# A simple way to mirror git repositories

```bash
cd repos
git clone --mirror https://source.example
cd repo.git
git remote add --mirror=push target https://target.example
```
