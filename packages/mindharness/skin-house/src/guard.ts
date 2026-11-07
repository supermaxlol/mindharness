/**
 * guard — Fire Station brake for the wallet.
 * If spend rate > earn rate for a window, force cheap mode.
 * Returns "ok" | "cheap-mode" | "shrink" | "dissolve"
 */

export type GuardState = {
  earnings: number;
  spend: number;
  turnsBelowFloor: number;
  floor: number; // reserve floor
};

export function guardDecision(s: GuardState): "ok" | "cheap-mode" | "shrink" | "dissolve" {
  if (s.turnsBelowFloor >= 5) return "dissolve";
  if (s.earnings < s.spend) return "cheap-mode";
  if (s.earnings - s.spend < s.floor) return "shrink";
  return "ok";
}
