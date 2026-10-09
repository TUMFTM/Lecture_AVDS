#include "abstraction_cpp/base_class_interface.hpp"

#include <iostream>

// High-level
void Abstraction::execute()
{
    std::cout << "I'm the interface." << std::endl;
}

void Parent::execute()
{
    std::cout << "I'm the base class." << std::endl;
}

// Low-level
void A::execute()
{
    std::cout << "I'm class A." << std::endl;
}

void B::execute()
{
    std::cout << "I'm class B." << std::endl;
}

int main()
{
    auto class_a = std::make_shared<A>();
    auto class_b = std::make_shared<B>();

    run_abstraction(class_a);
    run_base(class_b);
    class_b->execute();

    return 0;
}
