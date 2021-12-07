def clean(agent_location,location_status):
    if agent_location=="A" and location_status[0]==0:
        print("Position A is clean")
        agent_location="B"
        print("Moving agent to location B")
        return
    if agent_location=="A" and location_status[0]==1:
        print("Position A is dirty, Cleaning")
        location_status[0]=0
        print("Position A cleaned")
        agent_location="B"
        print("Moving agent to location B")
        return
    if agent_location=="B" and location_status[1]==0:
        print("Position B is clean")
        agent_location="A"
        print("Moving agent to location A")
        return
    if agent_location=="B" and location_status[1]==1:
        print("Position B is dirty, Cleaning")
        location_status[0]=0
        print("Position B cleaned")
        agent_location="A"
        print("Moving agent to location A")
        return

def main():
    agent_location="A"
    location_status=[0,0]
    user_input=1
    
    while user_input==1 :
        print("Enter Location A or B")
        location=input()
        status=[0,0]
        if location=="A" :
            print("Enter location status 0.clean 1.dirty")
            status[0]=int(input())
        elif location=="B" :
            print("Enter location status 0.clean 1.dirty")
            status[1]=int(input())
        else :
            print("Invalid Input")
        print("Agent position "+location)
        clean(location,status)
        print("Do you want to continue 0.No 1.Yes")
        user_input=int(input())
    
main()


