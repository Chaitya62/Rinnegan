# Name
- Rinnegan

# Tagline
- Blink up, before they dry up!

# The problem it solves
- Detects symptoms for Dry Eye Syndrome and Computer Vision Syndrome and employs methods to eradicate, or prevent it if you don't show any signs for the same.
- Analyses your blinking patterns while you're using your laptop accordingly and stimulates blinking by suitable scheduling various minute-long exercises and games.
- Enables people to involuntarily get used to the age old concentration and productivity technique, Pomodoro.

# Challenges we ran into
- We were bouncing off of all kinds of dreamy projects, some of which were too advanced to be built in 30 hours, while some were CRUD and API applications. 7 hours into the hackathon, it dawned upon us.
- Poor lighting leading to noisy data from the camera sensor.
- Originally we noticed that the pupil location moved a little when you blinked your eyes. This was a side effect of OpenCV's eye detection algorithm. We used the position of the pupil to derive it's acceleration from previous points and attempted to trigger off of this acceleration. We put a lot of effort in trying to calibrate this but in EE terms the signal was below the noise floor. There were as many false positives as true detections and we could not get an accurate system.

# Technologies we used 
`OpenCV` `PyGame` `Python`
