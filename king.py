from action import action
from message import Message

def the_end(Kate,King):
    #action('SetPosition('+charlie_earth.name+',Courtyard.Gate)')
    #action('CreateEffect('+charlie_earth.name+', Resurrection)')

    action('ShowDialog()')
    action('SetLeft(Kate)')
    action('SetRight(King)')

    Message('Kate: Hello King. Hear is the key which you asked me to get it from forest!')
    Kate_earth.camera()
    Message('King: I am so proud of you Kate. Thanks for getting back my Red Key!' )
    Message('Kate: Its my duty dear king!!')
    action('SetCameraMode(Track)')
    action('Face(Kate,King')
    action('WalkTo('King','Kate')')
    Message('King: In the form of rewards i am giving to you Gold coins.')
    action('TakeCoins('King','Kate')')
    Message('Kate:Thank you my lord King')
    action('CreateEffect(Happy,'Kate')')
    
    
    
