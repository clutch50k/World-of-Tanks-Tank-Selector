import tkinter as tk
from PIL import ImageTk, Image
import random

# List of tank classes, tiers and nations
tank_classes = ['light tank', 'medium tank', 'heavy tank', 'tank destroyer', 'artillery']
tank_tiers = list(range(1, 11))
nations = ['USA', 'Germany', 'Britain', 'France', 'USSR', 'China', 'Poland', 'Sweden', 'Czechoslovakia', 'Japan']

def generate_random_tank(selected_tiers, selected_classes, selected_nations):
    # Randomly select a tier, tank class and nation
    tier = random.choice(selected_tiers)
    tank_class = random.choice(selected_classes)
    nation = random.choice(selected_nations)

    return f"You got a Tier {tier} {tank_class} from {nation}"

def main():
    # Create the tkinter window
    window = tk.Tk()
    window.withdraw()  # Hide the window
    window.configure(bg="#262626")
    window.option_add("*Font", "Arial 18")  # make font larger

    # Create a header for the application
    header = tk.Label(window, text="What are We Going to Play?", bg="#262626", fg="#ffffff", font=("Arial", 24), pady=20)
    header.grid(row=0, column=0, columnspan=3)

    # Create a label for Tier selection
    tier_label = tk.Label(window, text="Select Tier", bg="#262626", fg="#ffffff")
    tier_label.grid(row=1, column=0, sticky='w', padx=30)

    # Create checkboxes for each tank tier and pack them in a single vertical column
    tier_vars = {tier: tk.IntVar(value=1) for tier in tank_tiers}  # all checked by default
    tier_frame = tk.Frame(window, bg="#262626")
    tier_frame.grid(row=2, column=0, sticky='nw', padx=30, pady=30)
    for tier in tank_tiers:
        var = tier_vars[tier]
        c = tk.Checkbutton(tier_frame, text=f"Tier {tier}", variable=var, bg="#262626", fg="#ffffff", selectcolor="#262626", activebackground="#262626", activeforeground="#ffffff")
        c.pack(anchor='w')

    # Create a label for Class selection
    class_label = tk.Label(window, text="Tank Class", bg="#262626", fg="#ffffff")
    class_label.grid(row=1, column=1, sticky='w', padx=30)

    # Create checkboxes for each tank class and pack them in a single vertical column
    class_vars = {tc: tk.IntVar(value=1) for tc in tank_classes}  # all checked by default
    class_frame = tk.Frame(window, bg="#262626")
    class_frame.grid(row=2, column=1, sticky='nw', padx=30, pady=30)
    for tank_class in tank_classes:
        var = class_vars[tank_class]
        c = tk.Checkbutton(class_frame, text=tank_class, variable=var, bg="#262626", fg="#ffffff", selectcolor="#262626", activebackground="#262626", activeforeground="#ffffff")
        c.pack(anchor='w')

    # Create a label for Nation selection
    nation_label = tk.Label(window, text="Nation", bg="#262626", fg="#ffffff")
    nation_label.grid(row=1, column=2, sticky='w', padx=30)

    # Create checkboxes for each nation
    nation_vars = {nation: tk.IntVar(value=1) for nation in nations}  # all checked by default
    nation_frame = tk.Frame(window, bg="#262626")
    nation_frame.grid(row=2, column=2, sticky='nw', padx=30, pady=30)
    for nation, var in nation_vars.items():
        c = tk.Checkbutton(nation_frame, text=nation, variable=var, bg="#262626", fg="#ffffff", selectcolor="#262626", activebackground="#262626", activeforeground="#ffffff")
        c.pack(anchor='w')

  
    # Load button image and create button
    img = ImageTk.PhotoImage(Image.open("button_randomize.png"))
    button = tk.Button(window, image=img, command=None)  # command will be set later
    button.image = img  # keep a reference of the image to avoid garbage collection
    button.grid(row=3, column=0, columnspan=3)

    
    # Create a label to show the result
    result_label = tk.Label(window, text="", bg="#262626", fg="#ffffff", pady=30)
    result_label.grid(row=4, column=0, columnspan=3)


    def on_button_click():
        # Get a list of selected tiers, tank classes and nations
        selected_tiers = [tier for tier, var in tier_vars.items() if var.get() == 1]
        selected_classes = [tc for tc, var in class_vars.items() if var.get() == 1]
        selected_nations = [nation for nation, var in nation_vars.items() if var.get() == 1]

        # Validate that at least one tier, class and nation have been selected
        if not selected_tiers or not selected_classes or not selected_nations:
            result_label.config(text="Please select at least one tier, one class and one nation.")
        else:
            # Generate and display a random tank
            result = generate_random_tank(selected_tiers, selected_classes, selected_nations)
            result_label.config(text=result)

    # Set the button's command now that result_label is defined
    button.config(command=on_button_click)

    window.deiconify()  # Show the window
    window.mainloop()

if __name__ == "__main__":
    main()