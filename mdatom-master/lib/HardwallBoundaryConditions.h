#pragma once

#include<vector>


/*!
 * This class modifies atoms at the boundary to prevent them going outside the box.
 * This assures that hard-wall boundary conditions are met.

 */

class HardwallBoundaryConditions{
public:
    static void adjustBoundary(int nat, double timeStep, std::vector<double> &positions, std::vector<double> &velocities, double const *box);

    static void adjustBoundary(int nat, double timeStep, std::vector<double> &positions, std::vector<double> &velocities, double const *box, double const *origin);
};