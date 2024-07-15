# Some introductory codes for Yue Wu's summer project at the University of Nottingham

# Server commands
## Screen commands
- Check active screen sessions
  ```sh
  screen -ls
  ```
- create a new screen
  ```sh
  screen -S session_name
  ```
- detach the screen session (within the session)
  ```sh
  ctrl + a + d
  ```
- detach the screen session (from outside the session)
  ```sh
  screen -XS session_name detach
  ```
- reattach the screen session
  ```sh
  screen -r session_name
  ```
