import sys
def check_for_success(command):

    #keep getting responces until the success of fail the given command is received
    while True:


        # Get response from Camelot
        received = input()

        # Return True is success response,else false for fail response
        if received =='succeeded ' + command:
            return True
        elif received.startswith('failed ' + command):
            return False


def action(command):
    print('start ' + command, flush=True)
    #sys.stdout.flush()
    #Call function to check for its success
    return check_for_success(command)

action('ShowMenu()')
action('HideMenu()')
action('CreateCharacter(Kate)')
action('SetClothing(Kate, Noble)')
action('SetExpression(Kate, Happy)')
action('SetHairStyle(Kate,Spiky)')
action('SetSkinColor(Kate, 5)')
action('SetEyeColor(Kate, Brown)')
action('SetCameraFocus(Kate)')
action('CreatePlace(Camp, ForestPath)')
action('SetPosition(Kate, Camp)')
action('CreateCharacter(Tom, A)')
action('SetClothing(Tom, Noble)')
action('SetExpression(Tom, Happy)')
action('SetHairStyle(Tom,Spiky)')
action('SetSkinColor(Tom, 4)')
action('SetEyeColor(Tom, Red)')
action('SetDialog(Hi I am Kate looking for lost Diamond)')
action('ShowDialog()')
action('Wait(4.5)')
action('HideDialog()')




while(True):
    input()
