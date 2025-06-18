Feature: Product management

  Scenario: List all products
    When I request the list of products
    Then I should receive a list of all products

  Scenario: Read a product by ID
    Given a product exists with id 1
    When I request the product with id 1
    Then I should receive the product details

  Scenario: Update a product
    Given a product exists with id 1
    When I update the product with id 1 with new data
    Then the product details should be updated

  Scenario: Delete a product
    Given a product exists with id 1
    When I delete the product with id 1
    Then the product should no longer exist

  Scenario: Search products by name
    When I search products by name "Gadget"
    Then I should receive products matching "Gadget"

  Scenario: Search products by category
    When I search products by category "Electronics"
    Then I should receive products in "Electronics"

  Scenario: Search products by availability
    When I search products by availability "true"
    Then I should receive products that are available
