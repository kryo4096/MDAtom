#include "HardwallBoundaryConditions.h"


void HardwallBoundaryConditions::adjustBoundary(int nat, double timeStep, std::vector<double> &positions, 
                                std::vector<double> &velocities, double const *box){

    double origin[3] = {0, 0, 0};

    adjustBoundary(nat, timeStep, positions, velocities, box, origin);
}

void HardwallBoundaryConditions::adjustBoundary(int nat, double timeStep, std::vector<double> &positions, 
                                std::vector<double> &velocities, double const *box, 
                                double const *origin){
    
    for(int i = 0; i < nat; ++i){
        for(int j = 0; j < 3; ++j){

            double under = origin[j] - box[j] / 2 - (positions[3*i + j] - velocities[3*i + j] * timeStep);
            double over = - origin[j] + box[j] / 2 + (positions[3*i + j] + velocities[3*i + j] * timeStep);

            if(under >= 0 || over >= 0) {
                velocities[3*i + j] *= -1;
            }

            positions[3*i + j] += (under >= 0) * 2 * (under)
                                + (over >= 0) * 2 * (-over);

        }
    }
}

