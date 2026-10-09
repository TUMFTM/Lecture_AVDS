// Copyright 2026 Daniel Esser
#pragma once

#include <memory>

// High-level
class Abstraction
{
public:
    Abstraction() = default;
    virtual void execute();
};
class Parent
{
public:
    Parent() = default;
    void execute();
};

inline void run_abstraction(std::shared_ptr<Abstraction> abstraction) { abstraction->execute(); }
inline void run_base(std::shared_ptr<Parent> parent) { parent->execute(); }

// Low-level
class A : public Abstraction
{
public:
    void execute() override;
};
class B : public Parent
{
public:
    void execute();
};