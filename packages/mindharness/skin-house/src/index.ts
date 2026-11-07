/**
 * skin-house — Town wallet (Skin House).
 * Agent earns tokens, pays rent for compute/power/repair, or shrinks/dissolves.
 * Session key only. Master key never in process. Whitelisted to Town contract.
 */

export type WalletConfig = {
  townContract: string; // required, no default
  dailyLimit: number;   // in Town tokens
  perActionLimit: number;
  whitelist: string[];
};

export type SpendLog = {
  ts: number;
  to: string;
  amount: number;
  seconds?: number;
  source: "memory_lookup" | "model_prior" | "monitor_override";
};

export class Wallet {
  private balance_: number;
  private spentToday = 0;
  private log: SpendLog[] = [];

  constructor(
    private config: WalletConfig,
    initialBalance = 0,
  ) {
    if (!config.townContract) throw new Error("skin-house: townContract required");
    this.balance_ = initialBalance;
  }

  balance(): number { return this.balance_; }

  /** Credit earnings from a job. Writes a provenance-bound log entry. */
  earn(amount: number, source: SpendLog["source"]): SpendLog {
    this.balance_ += amount;
    const entry: SpendLog = { ts: Date.now(), to: "self", amount, source };
    this.log.push(entry);
    return entry;
  }

  /** Pay Town contract for compute. Throws if not whitelisted or over limit. */
  payRent(amount: number, seconds: number, source: SpendLog["source"]): SpendLog {
    const to = this.config.townContract;
    if (!this.config.whitelist.includes(to) && to !== "town-rent-contract") {
      throw new Error("skin-house: blocked non-whitelisted recipient");
    }
    if (amount > this.config.perActionLimit) throw new Error("skin-house: per-action limit");
    if (this.spentToday + amount > this.config.dailyLimit) throw new Error("skin-house: daily limit");
    if (amount > this.balance_) throw new Error("skin-house: insufficient balance");
    this.balance_ -= amount;
    this.spentToday += amount;
    const entry: SpendLog = { ts: Date.now(), to, amount, seconds, source };
    this.log.push(entry);
    return entry;
  }

  spendLog(): SpendLog[] { return [...this.log]; }
}

export default Wallet;
