Feature: Product Management

  Scenario: Reading a Product
    Given the product list is loaded
    When I read product with id 1
    Then I should see product details

  Scenario: Updating a Product
    Given the product list is loaded
    When I update product with id 1 to name "Updated"
    Then the product name should be "Updated"

  Scenario: Deleting a Product
    Given the product list is loaded
    When I delete product with id 1
    Then product with id 1 should not exist

  Scenario: Listing All Products
    Given the product list is loaded
    When I list all products
    Then I should see multiple products

  Scenario: Searching a Product by Category
    Given the product list is loaded
    When I search products by category "books"
    Then I should see only products in category "books"

  Scenario: Searching a Product by Availability
    Given the product list is loaded
    When I search products by availability "true"
    Then I should see only available products

  Scenario: Searching a Product by Name
    Given the product list is loaded
    When I search products by name "Phone"
    Then I should see only products with name "Phone"
