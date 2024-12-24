from entities.Category_class import Category
from service.create_category.CreateCategoryInputBoundary import CreateCategoryInputBoundary
from service.create_category.CreateCategoryInputData import CreateCategoryInputData
from service.create_category.CreateCategoryOutputBoundary import CreateCategoryOutputBoundary

class CreateCategoryInteractor(CreateCategoryInputBoundary):
    #Override
    def execute(CreateCategoryInputData): 
        try:
            # Checks if both the category name and the money allocated is greater then 0.
            if (len(CreateCategoryInputData.input_name) > 0) or (CreateCategoryInputData.input_allocation > 0):
                pass
                # PrepareSuccesView here
                # Add Category to DAO
        except:
            pass
            # PrepareFailView here