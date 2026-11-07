// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/// TownRent — minimal rent contract for agent Town.
/// Landlord (you) sets tariffs. Agent session key pays. Others cannot drain.
contract TownRent {
    address public landlord;
    uint256 public pricePerSecond; // in wei
    bool public paused;

    event RentPaid(address indexed agent, uint256 amount, uint256 seconds);
    event TariffSet(uint256 pricePerSecond);
    event Paused(bool paused);

    modifier onlyLandlord() {
        require(msg.sender == landlord, "only landlord");
        _;
    }

    constructor() {
        landlord = msg.sender;
    }

    function setTariff(uint256 price) external onlyLandlord {
        pricePerSecond = price;
        emit TariffSet(price);
    }

    function setPaused(bool p) external onlyLandlord {
        paused = p;
        emit Paused(p);
    }

    function payRent(uint256 seconds) external payable {
        require(!paused, "paused");
        require(msg.value >= seconds * pricePerSecond, "insufficient");
        emit RentPaid(msg.sender, msg.value, seconds);
    }

    function withdraw() external onlyLandlord {
        (bool ok, ) = payable(landlord).call{value: address(this).balance}("");
        require(ok, "withdraw failed");
    }
}
