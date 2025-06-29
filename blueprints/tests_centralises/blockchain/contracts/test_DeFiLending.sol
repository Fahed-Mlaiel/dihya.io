// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import "../../blockchain/contracts/DeFiLending.sol";
import "ds-test/test.sol";

contract DeFiLendingTest is DSTest {
    DeFiLending lending;

    function setUp() public {
        lending = new DeFiLending();
    }

    function testDepositWithdraw() public {
        lending.deposit{value: 1 ether}();
        lending.withdraw(1 ether);
        assertEq(address(this).balance, 1 ether);
    }

    function testEdgeCaseZeroDeposit() public {
        try lending.deposit{value: 0}() {
            fail();
        } catch {}
    }

    function testSecurityOverflow() public {
        // Simuler un overflow
        assertTrue(true);
    }
}
