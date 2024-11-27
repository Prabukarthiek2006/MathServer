from django.shortcuts import render

def power_calculator(request):
    """
    A simple view to calculate power (P = I²R) and print outputs to the terminal.
    """
    print("Power Calculator view accessed")  
    power = None 
    if request.method == 'POST':
        print("POST request detected") 

        try:
            
            current = float(request.POST.get('current', 0)) 
            resistance = float(request.POST.get('resistance', 0)) 

            power = (current ** 2) * resistance

           
            print(f"Inputs received: Current = {current} A, Resistance = {resistance} Ω")
            print(f"Calculated Power: {power} W")

        except ValueError as e:
           
            print(f"Error: Invalid input. Details: {e}")
            power = "Error: Invalid input values"

    
    return render(request, 'calc.html', {'power': power})
