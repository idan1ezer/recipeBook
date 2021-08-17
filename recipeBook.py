import tkinter as tk

CAT_FONT = ("Comic Sans MS", 12)
MAIN_FONT = ("Apple SD Gothic Neo", 12)
SEARCH_FONT = ("Franklin Gothic Book", 12)
RECIPE_FONT = ("Ariel", 12)


class Recipe:
    def __init__(self, cat, name, plates, ingredients, method, photo_url):
        self.cat = cat
        self.name = name
        self.plates = plates
        self.ingredients = ingredients
        self.method = method
        self.photo_url = photo_url


boiled_egg = Recipe("Breakfast", "Boiled Eggs", 2, "eggs", None, None)
burger = Recipe("Meat", "Burger", 1, "bun, meat, mayo, pickles", None, None)
salad = Recipe("Salads", "Fresh Salad", 2, "Tomatoes, Cucumber, Onion, Olive Oil, Lemon", None, None)
salmon = Recipe("Fish", "Salmon", 1, "Salmon, Tariaki sauce, salt", None, None)
pizza = Recipe("Cheese", "Pizza", 4, "bread, sauce, cheese", None, None)
panakota = Recipe("Dessert", "Panakota", 2, "Milk, Maple syrup", None, None)

recipes = [boiled_egg, salad, burger, pizza, panakota]


class RecipeBook(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self, "My Recipe Book")
        tk.Tk.iconbitmap(self, "cooking.ico")
        tk.Tk.geometry(self, "1280x720")
        tk.Tk.resizable(self, False, False)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (StartPage, RecipesPage, SearchPage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg="#C2B8A3")

        btn_view_recipes = tk.Button(self, text="View Recipes", font=MAIN_FONT,
                                     command=lambda: controller.show_frame(RecipesPage))
        btn_search_recipe = tk.Button(self, text="Search Recipe", font=MAIN_FONT,
                                      command=lambda: controller.show_frame(SearchPage))
        btn_add_recipe = tk.Button(self, text="Add Recipe", font=MAIN_FONT)
        btn_rem_recipe = tk.Button(self, text="Remove Recipe", font=MAIN_FONT)

        btn_main_list = [btn_view_recipes, btn_search_recipe, btn_add_recipe, btn_rem_recipe]
        for opt in btn_main_list:
            opt.pack(pady=10, padx=10)


class RecipesPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Cat buttons
        btn_breakfast = tk.Button(self, text="Breakfast", font=CAT_FONT)
        btn_salads = tk.Button(self, text="Salads", font=CAT_FONT)
        btn_fish = tk.Button(self, text="Fish", font=CAT_FONT)
        btn_meat = tk.Button(self, text="Meat", font=CAT_FONT)
        btn_cheese = tk.Button(self, text="Cheese", font=CAT_FONT)
        btn_desserts = tk.Button(self, text="Desserts", font=CAT_FONT)

        btn_back = tk.Button(self, text="Back to Main", font=MAIN_FONT,
                             command=lambda: controller.show_frame(StartPage))

        btn_cat_list = [btn_breakfast, btn_salads, btn_fish, btn_meat, btn_cheese, btn_desserts, btn_back]
        for cat in btn_cat_list:
            cat.pack(pady=10, padx=10)


class SearchPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # search label & entry & search button
        lbl_search = tk.Label(self, text="Enter recipe name: ", font=SEARCH_FONT)
        ent_search = tk.Entry(self)
        btn_search = tk.Button(self, text="Search", font=SEARCH_FONT)  # command

        btn_back = tk.Button(self, text="Back to Main", font=MAIN_FONT,
                             command=lambda: controller.show_frame(StartPage))

        # packing lable & entry & button
        lbl_search.pack(pady=10, padx=10)
        ent_search.pack(pady=10, padx=10)
        btn_search.pack(pady=10, padx=10)
        btn_back.pack(pady=10, padx=10)

'''
class AddPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class RemPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class SingleRecipePage(tk.Frame):

    def __init__(self, parent, controller, *args):
        tk.Frame.__init__(self, parent)
        if type(args[0]) is Recipe:
            lbl_name = tk.Label(self, text=args[0].name, font=RECIPE_FONT)
            lbl_plates = tk.Label(self, text=args[0].plates, font=RECIPE_FONT)
            lbl_ingredients = tk.Label(self, text=args[0].ingredients, font=RECIPE_FONT)

        # page content
        # name, plates, ingredients, method, photo_url
        #

        btn_next_recipe = tk.Button(self, text="Next Recipe", font=MAIN_FONT)
        btn_prev_recipe = tk.Button(self, text="Previous Recipe", font=MAIN_FONT)
        btn_back_main = tk.Button(self, text="Back to Main", font=CAT_FONT)


        btn_back = tk.Button(self, text="Back to Main", font=MAIN_FONT,
                             command=lambda: controller.show_frame(StartPage))

        btn_cat_list = [btn_breakfast, btn_salads, btn_fish, btn_meat, btn_cheese, btn_desserts, btn_back]
        for cat in btn_cat_list:
            cat.pack(pady=10, padx=10)
            
        



    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x750")
        self.root.resizable(False, False)
        self.root.title("My Recipe Book")
        self.root.configure(bg = "#C2B8A3")

        self.categories = ["Breakfast", "Salads", "Fish", "Meat", "Cheese", "Desserts"]
        self.LblBreakfast = tk.Label()


    def startUp(self):
        self.root.mainloop()



def AddRecipe(recipe):
    global recipes

    if recipe not in recipes:
        recipes.append(recipe)
        return True
    else:
        return False


def RemoveRecipe(recipe):
    global recipes

    if recipe in recipe:
        recipes.remove(recipe)
        return True
    else:
        return False


def LoadNextRecipe():
    global index, recipes
    index += 1

    temp_recipe = recipes[index]

'''

# main

if __name__ == "__main__":
    rb = RecipeBook()
    rb.mainloop()
    # rb.startUp()
